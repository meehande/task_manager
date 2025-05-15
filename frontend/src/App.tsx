import { useState, useEffect } from 'react';
import { Task, CreateTaskInput } from './types/task';
import { taskApi } from './api/taskApi';
import { TaskForm } from './components/TaskForm';
import { TaskList } from './components/TaskList';

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [error, setError] = useState<string | null>(null);

  const handleCreateTask = async (input: CreateTaskInput) => {
    try {
      const newTask = await taskApi.createTask(input);
      setTasks((prev) => [...prev, newTask]);
    } catch (err) {
      setError('Failed to create task');
    }
  };

  const handleRunTask = async (id: string) => {
    try {
      const updatedTask = await taskApi.runTask(id);
      setTasks((prev) => prev.map((task) => (task.id === id ? updatedTask : task)));
    } catch (err) {
      setError('Failed to run task');
    }
  };

  const handleCancelTask = async (id: string) => {
    try {
      const updatedTask = await taskApi.cancelTask(id);
      setTasks((prev) => prev.map((task) => (task.id === id ? updatedTask : task)));
    } catch (err) {
      setError('Failed to cancel task');
    }
  };

  const handlePauseTask = async (id: string) => {
    try {
      const updatedTask = await taskApi.pauseTask(id);
      setTasks((prev) => prev.map((task) => (task.id === id ? updatedTask : task)));
    } catch (err) {
      setError('Failed to pause task');
    }
  };

  const handleResumeTask = async (id: string) => {
    try {
      const updatedTask = await taskApi.resumeTask(id);
      setTasks((prev) => prev.map((task) => (task.id === id ? updatedTask : task)));
    } catch (err) {
      setError('Failed to resume task');
    }
  };

  // Poll for task updates
  useEffect(() => {
    const interval = setInterval(async () => {
      const runningTasks = tasks.filter(
        (task) => task.status === 'in_progress' || task.status === 'paused'
      );
      
      for (const task of runningTasks) {
        try {
          const updatedTask = await taskApi.getTask(task.id);
          setTasks((prev) => prev.map((t) => (t.id === task.id ? updatedTask : t)));
        } catch (err) {
          console.error('Failed to update task:', err);
        }
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [tasks]);

  return (
    <div className="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
      <div className="relative py-3 sm:max-w-xl sm:mx-auto">
        <div className="relative px-4 py-10 bg-white mx-8 md:mx-0 shadow rounded-3xl sm:p-10">
          <div className="max-w-md mx-auto">
            <div className="divide-y divide-gray-200">
              <div className="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                <h1 className="text-2xl font-bold text-gray-900 mb-8">Task Manager</h1>
                
                {error && (
                  <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4">
                    {error}
                  </div>
                )}

                <TaskForm onSubmit={handleCreateTask} />
                
                <div className="mt-8">
                  <h2 className="text-xl font-semibold text-gray-900 mb-4">Tasks</h2>
                  <TaskList
                    tasks={tasks}
                    onRun={handleRunTask}
                    onCancel={handleCancelTask}
                    onPause={handlePauseTask}
                    onResume={handleResumeTask}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App; 