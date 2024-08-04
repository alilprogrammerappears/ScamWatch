# ScamWatch Full Documentation

## Table of Contents

<ul>
<li>1.0 Introduction</li>
<ul>
<li>1.1 The Creators</li>
<li>1.2 The Issue</li>
<li>1.3 Current Solutions</li>
</ul>
<li>2.0 ScamWatch</li>
<ul>
<li>2.1 Set Up Instructions</li>
<li>2.2 General Information & Uses</li>
<li>2.3 ScamWatch Features</li>
<li>2.4 ScamWatch Constraints & Limitations</li>
<li>2.5 Future Functionality and Improvement Possibilities</li>
</ul>
<li>3.0 Technical Details</li>
<ul>
<li>3.1 Tech Stack</li>
<li>3.2 Program Dependancies</li>
<li>3.3 Function Design</li>
<ul>
<li>3.3.1 RCA Application Blocking</li>
<li>3.3.2 Network Connection Blocking</li>
<li>3.3.3 One-Time Connections</li>
<li>3.3.4 Local and External Alerts</li>
<li>3.3.5 GUI</li>
</ul>
</ul>
</ul>
<br>

## 1.0 Introduction

### 1.1 The Creators
ScamWatch is a keystone project from four people: Anmol Mazoo, Arshdeep Singh, Kassandra Montgomery, and Molik Verma. It was created for INFO 4190 & INFO 4290 in 2024 for Kwantlen Polytechnic University's Bachelor of Technology in Information Technology (BTech in IT) program.

### 1.2 The Issue

<p>Today, thousands of people are getting scammed online every day, costing victims millions of dollars and often destroying lives. For example, in 2022, the Canadian Anti-Fraud Centre received nearly 71,000 reports and estimate that only up to 10% of fraud victims submit a report. Of the reported victims, the total monetary amount lost was approximately $500 million (Royal Canadian Mounted Police, 2023). This does not account, however, for the emotional and mental trauma these scams inflict.</p>

<p>In many scams, for example refund and tech support scams, the first critical goal of the scammer is to have the victim download a remote connection software and connect to their computer. From there, the details of the scam can vary, however, regardless of the persuasion tactics and the details of the scam, once this connection has been made, the scammer has full control over the victim’s computer and access to any stored private information.</p>

<p>Furthermore, many of RCA applications auto-run on start-up and stay minimized in the background, which means that the connection can be re-established provided the target’s computer is on and the software is running. Ultimately, this connection can result in identity fraud, bank account and other financial information access, ransomware attacks and installation of malicious software, extortion, and more.</p>

<p>While there are many people who can identify and avoid falling for these scams, there are many people who are unable to. These people may be older, have medical or health issues, are financially struggling, or are simply inexperienced or uneducated in cybersecurity and digital technology. These people can very easily be lured into these scams and be taken advantage of.</p>

### 1.3 Current Solutions
<p>Unfortunately, while there are some other applications that work to combat this issue, there are few full-fledged programs. Many systems that do try to combat the issue, are generally web browser plugins that block malicious sites. Examples of these include Malwarebytes, AdGuard, Privacy Badger, and numerous anti-virus software. There are two issues with this; firstly, these browser plugins often come with adware or require the user to purchase “premium” features for the best protection. Secondly, while the plugins provide protection for online activity, it is no longer effective once a remote connection application has been installed and is running on the computer.</p>

<p>There are four major applications that stand out, however: Seraph Secure, TheWindowsClub’s Windows Program Blocker, AppLocker, and Window’s Group Policy Editor. All of these applications have their uses; however they are not widely useful in all situations and, with the exception of SeraphSecure, they are not comprehensive. For example, the Window’s Group Policy Editor (WGPE) is a powerful tool that deploys group policies easily within an organization, including not allowing specific Windows applications to run. Similarly, AppLocker is included with Windows and operates based on deployed policies. It can additionally be used to export rules into WGPE and be used in conjunction. While these are helpful within organizations, they are applications that require intermediate to advanced computer knowledge and are not suitable for everyday users, not to mention non-tech savvy users.</p>

<p>For the audience that we are appealing to, non-tech savvy everyday users, SeraphSecure is by far the best option of these applications, although it is offered as a paid subscription. Their goal is specifically to stop scams from happening rather than being a universal program blocker. Due to this, while SeraphSecure does monitor background processes, it primarily is used to block malicious sites and alert when something suspicious happens or is downloaded. It achieves this by monitoring browsing data. Based on the content on the SeraphSecure website, it does not, however, terminate RCA’s that are currently running, and instead its focus is on alerting both the user and their appointed contact, or “guardian”.</p>
<br>

## 2.0 ScamWatch

### 2.1 Set Up Instructions
<p>In its current state, some aspects of ScamWatch have to be set up by the user installing it.</p>
<p>For example, for ScamWatch to run on start-up, it needs to be scheduled as a recurring task in the Windows Task Scheduler.</p>
<p>A future goal is to eliminate this need for set up, however that is restricted by our time and developer restraints as outlined in section 2.4. For more future plans and possibilities, please see section 2.5.</p>

#### 2.1.1 Running ScamWatch on Start-up
<p>To have ScamWatch run when the user's computer starts up, which is the highly recommended way to have ScamWatch run, users will need to create a scheduled task in the Windows Task Scheduler.</p>

<p>While this may seem daunting at first, don't worry - we're here to walk you through it!</p>

<b>Step 1:</b><br>
<p>In the Windows search bar, search "Task Scheduler", or press Win + R and then enter "taskschd.msc"</p>
<p>Then, along the right sidebar, under "Actions", click "Create Task"</p>

![](./Task%20Scheduler%20Screenshots/1_create%20task.png)

<br>
<b>Step 2:</b><br>
<p>In the wizard that pops up, type "ScamWatch" or something similar Under "Name".</p>
<p>Then, ensure the following options are checked: "Run whether user is logged in or not" and "Run with highest privilege".</p>
<p>Next, you'll need to choose what user or group to use. This can vary from person to person, but the user must have administrative privileges. Generally, it is easiest to use the "ADMINISTRATOR" user group, however if you have a user profile that is administrative, that will work too.</p><br>
<p>When Finished, it should look something like this:</p>

![](./Task%20Scheduler%20Screenshots/2_task%20settings_general.png)

<br>

<b>Step 3:</b><br>

<p>Click on the "triggers" tab and then click "new".</p>
<p>In the pop-up, choose "at start-up" from the "begin the task" option at the top and then press "okay"</p>

![](./Task%20Scheduler%20Screenshots/3_trigger.png)
<br>

<b>Step 4:</b><br>
<p>Click on the "Actions" tab and then click "new".</p>
<p>in the pop-up, choose "start a program" for "action" and then browse for the scamwatch_main.py file. Then click "okay".</p>

<br>

<b>Step 5:</b><br>
<p>Click on the "Conditions" tab. It should look like the screenshot below - with nothing checked:</p>

![](./Task%20Scheduler%20Screenshots/4_conditions.png)

<br>

<b>Step 6:</b><br>
<p>Click on the "Settings" tab and check the following options and then click "Okay"</p>
<ul>
    <li>Allow task to be read on demand</li>
    <li>If the running task does not end when requested, force it to stop</li>
</ul>

<p>It should look like this: </p>

![](./Task%20Scheduler%20Screenshots/4_settings.png)

<br>

<p>And that's it! Once you restart your computer, ScamWatch will be there to protect you!</p>


### 2.2 General Information & Uses

<p>ScamWatch is a downloadable software for Windows operating systems, designed to provide an extra layer of protection against common scams, specifically scams that involve the use of remote-control access (RCA) applications. The primary functions of this software are to block the installation of RCA applications, block remote connections, and notify the user when a remote connection is attempted. The secondary function of ScamWatch is to help educate the user in an effort to help promote awareness.</p>

<p>The most common use case for ScamWatch is for a loved one of a vulnerable user, such as an elderly or non-tech savvy person, to download ScamWatch onto their computer to constantly keep an eye out for potential scams and send an alert if something is caught. For example: Steve has an elderly grandparent, Meredith, who he is worried about getting scammed. She is not good with computers and tends to trust people easily. He hears about ScamWatch and downloads it onto Meredith's computer. He additionally creates an account and adds himself as a trusted contact, entering his email address.</p>

<p>One day, Meredith is talking to computer support, who in actuality is a scammer, and they try to have her download and use a remote control access application, such as TeamViewer. ScamWatch will not stop the download, however, when TeamViewer is ran, ScamWatch terminates the program, shows an alert to Meredith, and sends an email notification to Steve, informing both of them that this may be a potential scam. Furthermore, it provides a link that sends them to resources and steps they can take if they believe it is, in fact, a scam.</p>

<p>of course, Meredith (or another vulnerable user), may use ScamWatch themselves as well. A second use case, which we expect would be less common, but would still be possible, is for someone who may be part of a business and want to add an extra layer of protection onto the employee computers.</p>

<p>We do realize that there are situations where someone may need to connect to a user's computer for legitimate reasons. Due to this, if the user requires an RCA application for a legitimate use, they may either contact the person who set it up on their computer, for example Steve from earlier, to help unblock the application temporarily, or they may log into ScamWatch, themselves.</p>
<br>

### 2.3 ScamWatch Features

<p>Below are a list of features and functions that of ScamWatch. More technical details on how each function works will be expounded upon in section 3.0.
</p>
<ul>
    <li><strong>Process Monitoring and RCA Application Blocking</strong></li>
    <ul><li>ScamWatch monitors the user's computer for common RCA applications and stops them from running</li>
    </ul>
    <li><strong>Remote Connection Blocking</strong></li>
    <ul><li>As new RCA applications come out, there may be some that get unchecked by ScamWatch. To combat this, ScamWatch will be aware of remote connection attempts and terminate the connection.</li>
    </ul>
    <li><strong>External and Local Alerts</strong></li>
    <ul><li>ScamWatch provides two types of alerts: local and external. The local alert functions as a pop-up whenever ScamWatch detects something. External alerts are set up by the user and include an email and/or SMS alert to the provided email address/phone number. This is optional, but highly recommended.</li>
    </ul>
    <li><strong>Useful Educational Resources</strong></li>
    <ul><li>ScamWatch provides educational resources and trusted links on different scams, what to do if you believe you or someone you know is being scammed, and authorities you may contact. Note: This application is being developed in BC Canada, and some information may be region specific.</li>
    </ul>
    <li><strong>One-Time Connections</strong></li>
    <ul><li>For pre-determined, legitimate connections, users may pause ScamWatch's blocking functions through a setting accessible only after logging into an account.</li>
    </ul>
</ul>
<br>

### 2.4 ScamWatch Constraints & Limitations

<p>As ScamWatch is a project that has been implemented within a short timeframe and that we are students, there are constraints and limitations to be aware of. Our hope is that we will be able to improve and expand upon this software in the future. The following list outlines these constraints:</p>

<ul>
    <li><strong>Time Constraint</strong></li>
    <ul><li>ScamWatch is being implemented within the span of 4 months and while there are four developers, they are all enrolled in other classes and work full or part-time. This time constraint severely limits the possibilities of this software. For example, compatibility with multiple operating systems, the integration of AI, and a browser extension to block access to scam websites would be ideal functions, however they are not possible to implement within this timeframe.</li>
    </ul>
    <li><strong>Budget Constraint</strong></li>
    <ul><li>As this is a student project, there is a substantial budget constraint. This constraint will influence decisions regarding the services, tools, and programmatic options used.</li>
    </ul>
    <li><strong>Device Compatibility</strong></li>
    <ul><li>ScamWatch will currently only be compatible with modern Windows operating systems due to a lack of time and knowledge.</li>
    </ul>
    <li><strong>New Scams</strong></li>
    <ul><li>As new scams and new scam technology are constantly evolving, for long-term life, ScamWatch would need to be constantly updated, have access to common up to date anti-scam resources, or be integrated with AI, which is outside the scope of this project.</li>
    </ul>
    <li><strong>User Tech Literacy</strong></li>
    <ul><li>ScamWatch is created to protect users who may have low tech literacy which may impact the usability of the software. Ideally, there would be a website that has numerous how-to articles, however unfortunately this will not be implemented due to time.</li>
    </ul>
    <li><strong>Developer Abilities</strong></li>
    <ul><li>Some functions, such as the possibility of sending an alert to a different device or the use of multi-factor authentication, may be impacted by the developers’ knowledge and within this timeframe, may be limited.</li>
    </ul>
</ul>

<br>

### 2.5 Future Work


<br>

## 3.0 Technical Details
<p>This section will go through how exactly ScamWatch works and what it's built on.</p>

### 3.1 Tech Stack
<p>ScamWatch has been created using Python, utilizing its abilities to easily work with Windows OS interactions and its extensive collection of libraries. This includes TKinter for the creation of a GUI. Additionally being used is AWS for a small relational database that will be used to store information such as user login.</p>

### 3.2 Program Dependencies
<p>To run properly, ScamWatch needs Python and a number of Python libraries to be installed on the user’s machine. Many of the libraries come pre-installed with Python, however some do not and need to be installed separately. Our recommendation is to use pip via the command line to install the following:</p>
<ul>
    <li>psutil</li>
    <li>mysql</li>
    <li>pillow</li>
    <li>winshell</li>
    <li>win32com</li>
    <li>pythoncom</li>
    <li>tkinter</li>
</ul>


### 3.3 Function Design

#### 3.3.1 RCA Application Blocking

<p>The RCA application blocking feature is fairly straight forward. Using the psutils Python library, it monitors the process manager for processes that match a list of exe names. If it finds one, it terminates that program. It runs on a cycle, so that it consistantly continues monitoring even after it has terminated a program. As some processes will have sub-processes under the same name, Anydesk is an example of this, to prevent the alert being triggered multiple times, the exe name is added to a set called "warned_processes" once it is terminated, which gets cleared at the end of each cycle.</p>

<p>Some processes use administrative privileges, for example, TeamViewer. In order to interact with them, ScamWatch also needs administrative privileges. Due to this, as soon as ScamWatch starts up, it does a check to see if it has started with elevated privileges and if it didn't, attempts to re-start itself.</p>
<br>

#### 3.3.2 Network Connection Blocking

<p>In addition to blocking RCA applications from running, ScamWatch additionally attempts to block remote access network connections. Rather than continuously monitoring incoming packets however, ScamWatch adjusts firewall settings to block specific network ports that are commonly used by RCA applications. For example, ports 3389, 5938, 5900, and 6568. While it is true that future RCA applications may decide to use different ports, this will provide an extra layer of protection against commonly used remote access ports and the list may easily be updated in the future. Furthermore, this allows for legitimate connections and simplifies the process.</p>

<p>Similarly to the RCA app blocking function, adjusting firewall settings requires administrative privileges.</p>
<br>

#### 3.3.3 One-Time Connections

<p>As there are legitimate situations where a user may need someone to remotely access their computer, ScamWatch has the ability to allow a one-time connection. As the purpose of ScamWatch is to prevent these connections however, the connection allowance times out after 30 minutes. Furthermore, the user can access this setting only after they enter a password and an alert is trigged locally as well as sent to their trusted contact (if added).</p>

<p>The one-time connection feature essentially pauses the application. It stops the process monitoring for a period of time to allow for the use of an RCA application. Currently, the time is set to 30 minutes.</p>

<p>**NOTE**: In order for the One Time Connection to work, scamwatch.py <b>must</b> be running. If ScamWatch has been configured to start on computer start-up, it will automatically be running. This is something that will be improved upon in the future. For more information, refer to section 2.5: Future Work.</p>

<br>

#### 3.3.4 Local and External Alerts

<p><b><u>I don't know how this works yet other than a pop up being triggered when a connection happens or an RCA app is detected.</u></b></p>
<br>

#### 3.2.5 GUI

<p><b><u>I don't know how this works yet other than it uses TKinter (a framework that I don't know how to pronounce. T-K-inter? TehKinter?</u></b></p>
<br>
