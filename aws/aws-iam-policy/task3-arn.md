![AWS logo](https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg "AWS logo")


### [ARN Format for s3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies)

|  Resource Name    | ARN | Link  |
|      ---          | ---  | --- |
|      S3 accesspoint  |*arn:${Partition}:s3:${Region}:${Account}:accesspoint/${AccessPointName}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies "s3 arn link")|
|      S3 bucket  |*arn:${Partition}:s3:::${BucketName}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies "s3 arn link")|
|      S3 storagelensgroup  |*arn:${Partition}:s3:${Region}:${Account}:storage-lens-group/${Name}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies "s3 arn link")|
|      S3 object  |*arn:${Partition}:s3:::${BucketName}/${ObjectName}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies "s3 arn link")|

---
---

### [ARN Format for IAM](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-resources-for-iam-policies)

|  Resource Name    | ARN | Link  |
|      ---          | ---  | --- |
|      IAM mfa  |*arn:${Partition}:iam::${Account}:mfa/${MfaTokenIdWithPath}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-resources-for-iam-policies "IAM arn link")|
|      IAM role  |*arn:${Partition}:iam::${Account}:role/${RoleNameWithPath}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-resources-for-iam-policies "IAM arn link")|
|      IAM user  |*arn:${Partition}:iam::${Account}:user/${UserNameWithPath}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-resources-for-iam-policies "IAM arn link")|

---
---

### [ARN Format for EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies)

|  Resource Name    | ARN | Link  |
|      ---          | ---  | --- |
|      EC2 elastic-ip  |*arn:${Partition}:ec2:${Region}:${Account}:elastic-ip/${AllocationId}* | [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies "ec2 arn link")|
|      EC2 fleet  |*arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies "ec2 arn link")|
|      EC2 instance  |*arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies "ec2 arn link")|
|      EC2 image  |*arn:${Partition}:ec2:${Region}::image/${ImageId}*| [source](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies "ec2 arn link")|