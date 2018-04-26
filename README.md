# automated-aws-fileservers
Bishop Fox project with Ansible and Rundeck

Objective: Design and implement an automated file server with security integrated in the AWS instances. 

Completion: All of the Ansible plays and scripts were developed as a framework for implementing the concept.

Run the update_env.bash script before running the Ansible playbooks. Near future step, set the dependencies for API keys and file paths to a locked down and read-only dynamic inventory file. 

To make the ssh connection easier for yourself, run the following commands to bypass ssh passphrase prompt:
                              
                              1. ssh-agent bash
                              
                              2. cd .ssh/
                              
                              3. ssh-add <private key.pem>

Ansible - provisioning Playbooks and scripts:
                              
                              1. provisioning-aws.yml
                              
                              2. domain-generator.yml / dependent on subdomain_creator.py
                              
                              3. dns-setup.yml  / dependent on set_record.bash
                              
                              4. start-service.yml
                              
                              5. sf-creation.yml / dependent on sf-acct-creation.bash

Ansible - terminating Playbooks and scripts:
                             
                              1. dns-teardown.yml / dependent on delete-dns-record.py
                              
                              2. terminate-aws.yml 

run playbooks: ansible-playbook <play> 

Future goals for this project:
                             
                             - Properly hookup to front-end console that allows for user input to set the user's to the correct Seafile security roles. Plus, the Ansible playbooks can run smoothly. Finally, dashboard to see the status on the AWS instances.
                              
                              - Ansible playbook terminate-aws.yml needs to have json filtering search for the instance_ids value so that the developer does not need to hard code the instance id. Ansible configuration for better granular selection of AWS instances for terminating and configuring (use groups). Set a timer for terminating process for the AWS instances. Configure a faster process for Ansible to register running EC2 instances between the provisioning-aws.yml and domain-generator.yml or setup asynchronous tasks in playbooks.
                              
                              - Security wise, use the Ansible vault instead of environment variables. Security group and AWS firewall rules set to isolate the instances without shared ssh keys (maybe>). Plus, an AWS account seperated from other accounts with the account locked down as much as possible. 
                              - Design may want to look into a reliable uptime and cheaper vps provider for this project.
 
 Rundeck
   The download and installation process was easy.
   Configuration was not properly documented and assistance was slow; however there is a possible free trial that has support.
   The plugin for both Ansible and AWS EC2 was easy to download and install.
   The configuration of the AWS EC2 and Ansible plugins were again poorly documented and setbacks prevented from fully implementing its capabilities. The issue was the ec2 username was still stuck on the default and could not be changed based on the plugin's documentation for setting configuration. Plus, Rundeck documentation was never clear if the newest version of Rundeck was still able to use the AWS ec2 plugin.
   Recommend either testing the professional version of Rundeck or Ansible which has a paid front-end console with support. 
   
