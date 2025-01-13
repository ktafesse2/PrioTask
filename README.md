# Priority Task Scheduler

A task scheduling system implementing a priority queue using a min heap data structure. This project is designed to efficiently manage and schedule tasks based on their priority levels.

## Project Structure
```
priority-task-scheduler/
├── src/
│   ├── data_structures/
│   │   ├── min_heap.py      # MinHeap implementation
│   │   └── priority_queue.py # To be implemented
│   ├── models/
│   │   └── task.py          # Task model implementation
│   └── scheduler/
│       └── task_scheduler.py # To be implemented
├── tests/
│   └── test_min_heap.py     # MinHeap tests
└── README.md
```

## Current Implementation

### Completed Components
- MinHeap Implementation (`src/data_structures/min_heap.py`)
  - Basic heap operations (insert, extract_min, etc.)
  - Heapify functionality
  - Capacity management
  - Full test coverage

- Task Model (`src/models/task.py`)
  - Task representation with priority
  - Basic task attributes
  - Task comparison logic

## Next Steps

### Priority Queue Implementation
- Create PriorityQueue class using MinHeap
- Implement task-specific queue operations
- Add task management functionality

### Task Scheduler Development
- Time-based scheduling features
- Task categories and filtering
- Task persistence
- Analytics and monitoring

## Setup and Testing
1. Ensure you have Python installed
2. Clone the repository
3. Run tests:
```bash
pytest tests/
```
