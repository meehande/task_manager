import { Task, CreateTaskInput } from '../types/task';

const API_BASE_URL = 'http://localhost:8000/v1';

export const taskApi = {
  async createTask(input: CreateTaskInput): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/tasks/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(input),
    });
    if (!response.ok) throw new Error('Failed to create task');
    return response.json();
  },

  async getTask(id: string): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}`);
    if (!response.ok) throw new Error('Failed to fetch task');
    return response.json();
  },

  async runTask(id: string): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}/run`, {
      method: 'POST',
    });
    if (!response.ok) throw new Error('Failed to run task');
    return response.json();
  },

  async cancelTask(id: string): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}/cancel`, {
      method: 'POST',
    });
    if (!response.ok) throw new Error('Failed to cancel task');
    return response.json();
  },

  async pauseTask(id: string): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}/pause`, {
      method: 'POST',
    });
    if (!response.ok) throw new Error('Failed to pause task');
    return response.json();
  },

  async resumeTask(id: string): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/tasks/${id}/resume`, {
      method: 'POST',
    });
    if (!response.ok) throw new Error('Failed to resume task');
    return response.json();
  },
}; 