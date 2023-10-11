# Event-Driven Architecture with Python

## Overview

This repository demonstrates an event-driven architecture in Python, which is a design pattern that allows you to create loosely coupled and highly extensible systems. In this architecture, events are central to communication between components, making it easy to add new functionality without modifying existing code.

## Project Structure

The project structure is organized as follows:


- **`app/`**: The main package of the project.

- **`main.py`**: The entry point of the application where services are executed.

- **`services.py`**: Contains the actual services where events may occur.

- **`event_functions.py`**: Contains event functions that can be triggered by events.

- **`events.py`**: Defines the core event system with `register_event` and `dispatch` functions.

- **`bootstrap.py`**: Initialization file where events are registered.

## Event System

The `events.py` module provides a simple yet powerful event system. It defines the following functions:

- `register_event(event_name, event_function)`: Registers event functions for a specific event name.

- `dispatch(event_name, *args, **kwargs)`: Dispatches an event by name, triggering all registered event functions for that event.

## Initialization and Usage

The `bootstrap.py` module serves as the initialization point for the application. In this file, events are registered using the `register_event` function.

## Getting Started

1. Clone this repository:

   ```bash
   git clone git@github.com:DelivceNdegwa/Python-Event-Based-Architecture.git

2. Navigate to the project directory:
   ```bash
   cd event-driven-architecture-python

3. Run the application:
   ```bash
   python app/main.py
   or
   python -m app.main


