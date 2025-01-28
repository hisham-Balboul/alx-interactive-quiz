# Quiz App

Welcome to the Quiz App! This repository contains the source code for a fully functional, interactive quiz application built with modern web technologies. The app is designed to provide an engaging quiz experience for users, track scores, and maintain a leaderboard for competitive fun.

# Features

## Frontend

User Interface: A sleek, responsive, and user-friendly interface designed using Vue 3 and Tailwind CSS.

Dynamic Quiz Flow: Users can answer multiple-choice questions with real-time feedback on their answers.

Timer: Each question is timed to keep the game exciting and challenging.

Results: A detailed results page showing the user's score at the end of the quiz.

Leaderboards: Allows users to view scores for different quiz categories and compare their rankings.

## Backend

Flask API: A Python backend powered by Flask handles data processing and provides RESTful endpoints for the frontend.

Database: Leaderboard entries and quiz data are managed using SQLAlchemy and stored in a relational database.

CORS Support: Ensures smooth communication between the frontend and backend.

## Additional Features

Authentication: Users can register and log in to track their quiz performance (WiP).

Category-based Quizzes: Quizzes are organized into categories, allowing users to choose topics of interest.

Leaderboard Management: Tracks top performers across categories and displays the rankings in a table.

# Project Structure

## Frontend

The frontend is implemented using Vue.js and is located in the /frontend directory.

components: Contains reusable UI components like quiz questions, leaderboard, and results.

views: Includes pages such as Home, Quiz, Results, and Leaderboards.

store: Vuex store for state management (e.g., quiz data, user session, etc.).

assets: Static files such as images and stylesheets.

## Backend

The backend is implemented using Flask and is located in the /backend directory.

app: Main application folder containing routes, controllers, and models.

routes: Contains API endpoints for quiz logic and leaderboard management.

models: Defines database models such as Leaderboard.

controllers: Handles business logic and integrates with database models.

extensions: Handles third-party integrations, such as database setup and CORS.

services: Contains helper functions for database interactions and data processing.
