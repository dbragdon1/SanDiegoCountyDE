# SanDiegoCountyDE

I wanted to create a local ETL system for processing San Diego County health data using airflow and a raspberry pi. The San Diego County data portal claims that this data is updated every evening, and I wanted to use this fact to test out airflow's scheduling services. At the end of the day, I wanted to build a system that would mimic a real airflow job, which runs continuously in the background and processes jobs according to a specific schedule. All of this with the added benefit that I could start, stop, and schedule airflow jobs from my main machine.


Another reason I wanted to try this is because, at the time of writing this, there weren't many tutorials out there for Airflow 2.0

192.168.1.131

## Setup

I'm using a raspberry pi 3 that I have preconfigured for SSH capabilities. Here's the OS info:

```
Static hostname: raspberrypi
      Icon name: computer
     Machine ID: cd27af819e6f4711838f6e2657c8672e
        Boot ID: 23cb16686b23465ab0d578a84ea04563
Operating System: Raspbian GNU/Linux 10 (buster)
         Kernel: Linux 5.10.17-v7+
   Architecture: arm
```

Next I created a virtual environment on my rpi so that airflow's installation didn't mess up any dependencies.


On the raspberry pi, airflow wouldn't run correctly until I changed the default secret key. I was able to directly edit the environment variable to fix this:

```bash
export AIRFLOW__WEBSERVER__SECRET_KEY=newsecretkey
```

After this I was able to start up the server through SSH on my main machine:

```console
pi@192.168.1.131:~$ airflow scheduler & airflow webserver
```

After going through the regular motions of starting up airflow (initializing db, starting webserver and scheduler, etc.) I began writing some DAGs for ingesting and processing the data that I want to create a snapshot of.





## The DAGs
