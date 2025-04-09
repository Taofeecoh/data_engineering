## TASK 1
Create an IAM user and attach a custom policy that satisfy the below condition
The user should only have access to see the list of files on any bucket name that has the word spark-job in s3. 
Please you need to use pattern matching to match the buckets with the word spark-job
However, The user should be able to delete any file in the bucket spark-job-data-input in the folder dumps except for the files that ends with csv.
Please use pattern matching to exclude the csv.

## TASK 2
Using the same user created above, create another custom-policy that will allow the user to only
Create an IAM user if the word engineer starts it. Basically if the user creates a user called daniel for example, the user should get permission denied, but when the user creates the user like this engineer_daniel, it should be created.

## TASK 3

Please list the ARN format/pattern for the below list of AWS resources. Please note that the bold part is the service and the one at the front is the resource, for example S3 is the service and accesspoint is the resource
- S3 accesspoint
- S3 bucket
- S3 storagelensgroup
- S3 object
- IAM mfa
- IAM role
- IAM user
- EC2 elastic-ip
- EC2 fleet
- EC2 instance
- EC2 image

~INSTRUCTIONS
Please have everything pushed to your github repository
For question 3, make sure you also add the link to the official AWS documentation of where you found the ARN format.
Please make sure you test this to ensure all policies are working
Submission date is before the next class on Thursday.
Failure to submit this exercise will attract a VERY BIG CONSEQUENCE 
Failure to answer the 3 exercise correctly will attract a VERY BIG CONSEQUENCE~
