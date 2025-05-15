# Task Manager Frontend

A React + TypeScript frontend for the Task Manager application.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The application will be available at http://localhost:5173

## Features

- Create new tasks with title and description
- Run, pause, resume, and cancel tasks
- Real-time progress tracking for running tasks
- Clean and responsive UI with Tailwind CSS

## Development

- Built with React 18 and TypeScript
- Uses Vite for fast development and building
- Styled with Tailwind CSS
- Implements polling for real-time task updates

## Building for Production

To create a production build:

```bash
npm run build
```

The built files will be in the `dist` directory. 


## Deployment


```bash 
cd frontend
docker build -f ./deployment/Dockerfile -t frontend:latest .
```

