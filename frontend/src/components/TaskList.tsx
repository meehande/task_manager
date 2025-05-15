import { Task, TaskStatus } from '../types/task';

interface TaskListProps {
  tasks: Task[];
  onRun: (id: string) => void;
  onCancel: (id: string) => void;
  onPause: (id: string) => void;
  onResume: (id: string) => void;
}

export function TaskList({ tasks, onRun, onCancel, onPause, onResume }: TaskListProps) {
  return (
    <div className="space-y-4">
      {tasks.map((task) => (
        <div key={task.id} className="bg-white p-4 rounded-lg shadow">
          <div className="flex justify-between items-start">
            <div>
              <h3 className="text-lg font-medium text-gray-900">{task.title}</h3>
              <p className="mt-1 text-sm text-gray-500">{task.description}</p>
            </div>
            <span className={`px-2 py-1 text-xs font-medium rounded-full ${
              task.status === TaskStatus.COMPLETED ? 'bg-green-100 text-green-800' :
              task.status === TaskStatus.IN_PROGRESS ? 'bg-blue-100 text-blue-800' :
              task.status === TaskStatus.PAUSED ? 'bg-yellow-100 text-yellow-800' :
              task.status === TaskStatus.CANCELLED ? 'bg-red-100 text-red-800' :
              'bg-gray-100 text-gray-800'
            }`}>
              {task.status}
            </span>
          </div>
          
          {task.status === TaskStatus.IN_PROGRESS && (
            <div className="mt-2">
              <div className="w-full bg-gray-200 rounded-full h-2.5">
                <div
                  className="bg-blue-600 h-2.5 rounded-full"
                  style={{ width: `${task.progress}%` }}
                ></div>
              </div>
              <p className="mt-1 text-sm text-gray-500">{Math.round(task.progress)}% complete</p>
            </div>
          )}

          <div className="mt-4 flex space-x-2">
            {task.status === TaskStatus.PENDING && (
              <button
                onClick={() => onRun(task.id)}
                className="px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded hover:bg-blue-700"
              >
                Run
              </button>
            )}
            {task.status === TaskStatus.IN_PROGRESS && (
              <>
                <button
                  onClick={() => onPause(task.id)}
                  className="px-3 py-1 text-sm font-medium text-white bg-yellow-600 rounded hover:bg-yellow-700"
                >
                  Pause
                </button>
                <button
                  onClick={() => onCancel(task.id)}
                  className="px-3 py-1 text-sm font-medium text-white bg-red-600 rounded hover:bg-red-700"
                >
                  Cancel
                </button>
              </>
            )}
            {task.status === TaskStatus.PAUSED && (
              <>
                <button
                  onClick={() => onResume(task.id)}
                  className="px-3 py-1 text-sm font-medium text-white bg-green-600 rounded hover:bg-green-700"
                >
                  Resume
                </button>
                <button
                  onClick={() => onCancel(task.id)}
                  className="px-3 py-1 text-sm font-medium text-white bg-red-600 rounded hover:bg-red-700"
                >
                  Cancel
                </button>
              </>
            )}
          </div>
        </div>
      ))}
    </div>
  );
} 