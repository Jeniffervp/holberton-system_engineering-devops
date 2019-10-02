# 0x18. Webstack monitoring

### Background Context

“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

Application monitoring: getting data about your running software and making sure it is behaving as expected
Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

### Task

| Task name | Description |
| --- | --- |
| 0. Sign up for Datadog and install datadog-agent | Sign up for Datadog Install datadog-agent on web-01 Create an application key Create the answer file 0-setup_datadog with your API key on the first line of the file, and your application key on the second |
| 1. Monitor some metrics | Set up a monitor that checks the number of read requests issued to the device per second. Set up a monitor that checks the number of write requests issued to the device per second. |
| 2. Create a dashboard | Create a new dashboard. Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like. Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API |