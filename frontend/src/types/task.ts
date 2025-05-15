export enum TaskStatus {
  PENDING = "pending",
  IN_PROGRESS = "in_progress",
  PAUSED = "paused",
  COMPLETED = "completed",
  CANCELLED = "cancelled",
}

export interface Task {
  id: string;
  title: string;
  description: string;
  status: TaskStatus;
  progress: number;
}

export interface CreateTaskInput {
  title: string;
  description: string;
} 