## **Who Is This For?**

We are looking for mission-driven Full Stack Engineers who enjoy building impactful and scalable applications. You will be contributing to a transformative healthcare product that supports AI-driven solutions, requiring a strong focus on security, scalability, and usability.

## **Task Overview**

You will build a full-stack web application that allows users to manage and execute "tasks." These tasks simulate long-running operations that can be started, monitored, paused, resumed, or cancelled.

Your implementation should include:

- A basic frontend UI for task management.
- A backend API to process and track tasks.
- A Dockerised setup to allow easy deployment and execution.
- The ability to run both frontend and backend locally with minimal setup.

## **Core Requirements**

### **1. Task Management UI (Frontend)**

Build a simple web app that allows users to create, run, and manage tasks. The UI should include:

- **Task Creation & Display**
    - A form to define and add a new task (e.g., task title and description).
    - A list to display all created tasks.
- **Task Operations**
    - A button to "Run" each task, updating its status to "In Progress."
    - A "Cancel" button to stop a task.
- **Task Status & Feedback**
    - Display the current status of each task (e.g., "Completed," "Cancelled").
    - (Nice-to-have) Show a progress indicator for running tasks.

### **2. Task Processing API (Backend)**

Create an API to manage tasks, including:

- **Task Execution**
    - An endpoint to receive a task request and simulate execution
    - Tasks should take ~30 seconds to complete.
    - Return dummy results (e.g., "Task complete!").

### 3. Bonus (if you have time)

**Pause and Resume Functionality**

**Task Management UI (Frontend)** 

- A "Pause" button to temporarily stop an ongoing task.
- A "Resume" button to continue a paused task.

**Task Processing API (Backend)** 

- Pause
- Resume

### **4. Dockerisation & Deployment**

Ensure the entire application can be run using Docker.

- Provide a **Dockerfile** for both frontend and backend.
- Document how to build and run the application in the **README**.

## **Technical Guidelines**

- You can use any programming language and framework of your choice (e.g., React, Vue, Angular for frontend; Node.js, Python, Go for backend).
- The frontend should integrate with the real backend API.
- Prioritise clear and well-structured code.
- Feel free to leverage AI tools (e.g., GitHub Copilot, ChatGPT) to assist with implementation, but clearly document where and how AI was used with comments in your code.

## **Deliverables**

Submit your solution as a **GitHub repository or ZIP file**, including:

1. All source code for frontend and backend.
2. A **README** explaining:
    - How to set up and run the project.
    - Key technical decisions and any assumptions made.
    - Testing instructions (if applicable).
3. Docker configuration files (Dockerfile, Docker Compose).

---

Good luck! We're excited to see your approach 🚀