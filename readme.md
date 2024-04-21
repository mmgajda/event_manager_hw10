## Issues

1) [Username Validation Tests](https://github.com/mmgajda/event_manager_hw10/issues/7)

2) [Enhance Profile Picture Tests](https://github.com/mmgajda/event_manager_hw10/issues/5)

3) [Comprehensive tests of registration format](https://github.com/mmgajda/event_manager_hw10/issues/3)

4) [Verification of hashing algorithm and password storage](https://github.com/mmgajda/event_manager_hw10/issues/7)

5) [Implementation of Password History Logging and Enforcement](https://github.com/mmgajda/event_manager_hw10/issues/9)

## Dockerhub Image

## Reflection   

  The first thing that really stuck out for me was how difficult it can be to understand a code base with so many parts.  This repository isn't large when you consider enterprise and professional applications, but it has far more moving pieces than anything I have done at NJIT or personally thus far.  QA, testing, and improving the code must begin with having a good understanding of how each part works and how it works together.
  This assignment also helped me to understand just how many things must be accounted for when any kind of user input is handled.  All input must be sanitized and validated so that things can work smoothly and also to prevent any kind of malicious input, code injection, etc.
  It is also very important that everything that is protected by login remains secure as well, and to this end it is important to institute aggressive policies towards password creation, hashing, storage, and controls for login.  In testing I realized that there were several issues with input at user creation and that there did not seem to be any storage of previous passwords.
  I created Github Issues as I came across these problems.  I then created a new branch to troubleshoot the code and implementation.  When everything was working I would push it to Github, create/merge the pull request, and close the issue.




1. **GitHub Repository Link**: Ensure that your repository is well-organized and includes:
  - Links to five closed issues, each with accompanying test code and necessary application code modifications.
  - Each issue should be well-documented, explaining the problem, the steps taken to resolve it, and the outcome. Proper documentation helps others understand your work and facilitates future maintenance.
  - All issues should be merged into the main branch, following the Git workflow and best practices.

2. **Updated README**: Replace the existing README with:
  - Links to the closed issues, providing easy access to your work.
  - Link to project image deployed to Dockerhub.
  - A 2-3 paragraph reflection on what you learned from this assignment, focusing on both technical skills and collaborative processes. Reflect on the challenges you faced, the solutions you implemented, and the insights you gained. This reflection helps solidify your learning and provides valuable feedback for improving the assignment in the future.

## Grading Rubric

| Criteria                                                                                                                | Points |
|-------------------------------------------------------------------------------------------------------------------------|--------|
| Resolved 5 issues related to username validation, password validation, and profile field edge cases                      | 30     |
| Resolved the issue demonstrated in the instructor video                                                                 | 20     |
| Increased test coverage to 90% by writing comprehensive test cases                                                      | 20     |
| Followed collaborative development practices using Git and GitHub (branching, pull requests, code reviews)              | 15     |
| Submitted a well-organized GitHub repository with clear documentation, links to closed issues, and a reflective summary | 15     |
| **Total**                                                                                                               | **100**|

## Resources and Documentation

- **Instructor Videos and Important Links**:
 - [Introduction to REST API with Postgres](https://youtu.be/dgMCSND2FQw) - This video provides an overview of the REST API you'll be working with, including its structure, endpoints, and interaction with the PostgreSQL database.
 - [Assignment Instructions](https://youtu.be/TFblm7QrF6o) - Detailed instructions on your tasks, guiding you through the assignment step by step.
 - [Git Command Reference I created and some explanation for collaboration with git](git.md)
 - [Docker Commands and Running The Tests in the Application](docker.md)
 - Look at the code comments:
    - [Test Configuration and Fixtures](tests/conftest.py)
    - [API User Routes](app/routers/user_routes.py)
    - [API Oauth Routes - Connection to HTTP](app/routers/oauth.py)
    - [User Service - Business Logic - This implements whats called the service repository pattern](app/services/user_service.py)
    - [User Schema - Pydantic models](app/schemas/user_schemas.py)
    - [User Model - SQl Alchemy Model ](app/models/user_model.py)
    - [Alembic Migration - this is what runs to create the tables when you do alembic upgrade head](alembic/versions/628adcb2d60e_initial_migration.py)
    - See the tests folder for all the tests

 - API Documentation: `http://localhost/docs` - The Swagger UI documentation for the API, providing information on endpoints, request/response formats, and authentication.
 - Database Management: `http://localhost:5050` - The PGAdmin interface for managing the PostgreSQL database, allowing you to view and manipulate the database tables.

- **Code Documentation**:
 The project codebase includes docstrings and comments explaining various concepts and functionalities. Take the time to read through the code and understand how different components work together. Pay attention to the structure of the code, the naming conventions used, and the purpose of each function or class. Understanding the existing codebase will help you write code that is consistent and integrates well with the project.

- **Additional Resources**:
 - [SQLAlchemy Library](https://www.sqlalchemy.org/) - SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of tools for interacting with databases, including query building, database schema management, and data serialization. Familiarize yourself with SQLAlchemy's documentation to understand how it is used in the project for database operations.
 - [Pydantic Documentation](https://docs.pydantic.dev/latest/) - Pydantic is a data validation and settings management library for Python. It allows you to define data models with type annotations and provides automatic validation, serialization, and deserialization. Consult the Pydantic documentation to understand how it is used in the project for request/response validation and serialization.
 - [FastAPI Framework](https://fastapi.tiangolo.com/) - FastAPI is a modern, fast (high-performance) Python web framework for building APIs. It leverages Python's type hints and provides automatic API documentation, request/response validation, and easy integration with other libraries. Explore the FastAPI documentation to gain a deeper understanding of its features and how it is used in the project.
 - [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/index.html) - Alembic is a lightweight database migration tool for usage with SQLAlchemy. It allows you to define and manage database schema changes over time, ensuring that the database structure remains consistent across different environments. Refer to the Alembic documentation to learn how to create and apply database migrations in the project.

These resources will provide you with a solid foundation to understand the tools, technologies, and concepts used in the project. Don't hesitate to explore them further and consult the documentation whenever you encounter challenges or need clarification.

## Conclusion

This assignment is designed to challenge you, help you grow as a developer, and prepare you for the real-world responsibilities of a Software QA Analyst/Developer. By working on realistic issues, collaborating with your team, and focusing on testing and quality assurance, you will gain valuable experience that will serve you throughout your career.

Remember, the goal is not just to complete the assignment but to embrace the learning journey. Take the time to understand the codebase, ask questions, and explore new concepts. Engage with your team members, seek feedback, and learn from their experiences. Your dedication, curiosity, and willingness to learn will be the key to your success in this role.

We are excited to have you on board and look forward to seeing your contributions to the project. Your fresh perspective and skills will undoubtedly make a positive impact on our team and the quality of our software.

If you have any questions or need assistance, don't hesitate to reach out to your mentor or team lead. We are here to support you and ensure that you have a rewarding and enriching experience.

Once again, welcome to the Event Manager Company! Let's embark on this exciting journey together and create something remarkable.

Happy coding and happy learning!
