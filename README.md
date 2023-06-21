# AWS-Explorer

A Python toolset to explore AWS account features

# Requirements

Have AWS CLI installed locally - see below.

# Examples

```
 % aws sts get-caller-identity       
{
    "UserId": "AIDAVB2ZOJ53E7X46H3BW",
    "Account": "347543064438",
    "Arn": "arn:aws:iam::347543064438:user/plh"
}
```


# Utilities

See b3 sub-directory for a bunch of stand alone scripts for querying various AWS features




# Installing the AWS CLI

Check out - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## MacOS

If you have sudo permissions, you can install the AWS CLI for all users on the computer. We provide the steps in one easy to copy and paste group. See the descriptions of each line in the following steps.

```
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
```

Download the file using the curl command. The -o option specifies the file name that the downloaded package is written to. In this example, the file is written to AWSCLIV2.pkg in the current folder.

 $ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"

Run the standard macOS installer program, specifying the downloaded .pkg file as the source. Use the -pkg parameter to specify the name of the package to install, and the -target / parameter for which drive to install the package to. The files are installed to /usr/local/aws-cli, and a symlink is automatically created in /usr/local/bin. You must include sudo on the command to grant write permissions to those folders.

 $ sudo installer -pkg ./AWSCLIV2.pkg -target /

After installation is complete, debug logs are written to /var/log/install.log.

To verify that the shell can find and run the aws command in your $PATH, use the following commands.

```
$ which aws
/usr/local/bin/aws 
$ aws --version
aws-cli/2.4.5 Python/3.8.8 Darwin/18.7.0 botocore/2.4.5
```

If the aws command cannot be found, you may need to restart your terminal or follow the instructions in Adding the AWS CLI to your path.


