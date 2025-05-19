# github-search-query

### What I didn't complete in the assignment
- Query validation - To make sure the query is correct and if not print an error and try the next one
- Pagination - Currently I only show the first 30 results. I need to make sure that it will display 100 items per page and cycle through the pages to add all the items to the final list.

### What I need to do to get this app to production
- Making the main function asynchronous so multiple people could process their files simuteniosly.
- Making the individual queries in a single file run asynchronously so that a single file proccessing will be faster.
- Add unit tests to make sure everything is working and new changes don't break anything.
- Add CI/CD that will make sure everything is working (via the tests) package and containerize the service and upload it to the correct environment.
- If the client is not in a hurry to get his results, perhaps using a scheduling tool like Airflow to schedule jobs at cirtain time so not all of them will happen at the same time.
- Using a cache to save the results of some common queries so that the service will not need to reach as much to the github API (We only get 10 request per minute).
