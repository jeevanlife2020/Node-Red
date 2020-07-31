# Node-Red-Flow

![alt text](https://github.com/jeevanlife2020/Node-Red/blob/master/node-red-flow-screenshot.PNG?raw=true)

## Working flow:

*  **Inject** node is automatically triggered in a interval of specific time.

* Once **Inject** node gets triggered, **Total_usage** random node is called. Where a random number is generated within the specific range.

* From **Total_usage** node a function is getting called where total_usage is stored in payload variable.

* In the **Flow_Rate** random node, a random number is generated within the specific range for Flow_Rate. Which is stored in payload variable.

* **Cloudant out** is used to insert the data to cloudant.

* **Data Fetchung from cloudant In** node is used to fetch the last 3 flow rate. 

* In the **Flow Rate checking to send mail** function, its checking whether flow rate is constant or not.

* If Flow rate is constant, a **Switch** node is used to send the mail to the user for notification.
