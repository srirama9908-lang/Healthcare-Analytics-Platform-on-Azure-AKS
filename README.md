1. Code pushed to GitHub
2. CI/CD builds image + deploys via Helm
3. Kubernetes updates pods

4. git-sync pulls latest DAGs

5. Scheduler parses DAGs
6. Scheduler pushes tasks → Redis

7. Workers pull from Redis
8. Workers execute tasks

9. Results + status → stored in Postgres

10. API/Webserver reads Postgres → shows UI
