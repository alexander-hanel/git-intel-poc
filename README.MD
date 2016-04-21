### TL;DR
Git is awesome for tracking code. Why not use it for tracking malware families and campaigns?

### Motivation 
In the past couple of days there has been some talk on Twitter about tracking Ransomware families.  The initial energy has focused on creating a [spreadsheet](https://docs.google.com/spreadsheets/d/1TWS238xacAto-fLKh1n5uTsdijWdCEsGIM0Y0Hvmc5g/edit#gid=0) for tracking ransomware families and their indicators. I'm not a big fan of spreadsheets. They are useful for modeling of atomic values but don't provide value when trying to understand a threat group or family of malware. Rather than using a spreadsheets I'd like to propose using Git for tracking malware families. In theory, Git can be used for tracking families of malware, threat groups or exploit kits. 

#### Why use Git?

 - Large community of Git users. 
 - Simple format. 
 - Easy to track changes. 
	 - Merges can be used to track modifications. 
	 - Senior analyst can review merges by junior analyst. 
 - Role based. 
	 - Public, private or hidden from selected individuals . 
 - Ability to link to third party tools. 
 - Can be automated.
 - Accessible from any where. 
 - Can be edited from browser, command line or text editor. 

#### Why not use Git?

 - Simple format, not easily query able.  
 - Constant merging. 
 - Parent and child pages must both be edited to show a relationship. 
 - Don't like change.  

#### How?
For starters we'll need a couple of items. The first is a malware template, a set of malware families and a Git repo. For the malware template I'm going to use [MAT](https://bitbucket.org/Alexander_Hanel/mat), the families will be a set of banking malware (the ransomware list would work for anyone doing the at home version) and a repo such as GitHub or BitBucket. The structure of the repo is simple. The root directory contains a `README.md` and a directory named `families`. The `README.md` will be the parent page that contains a list of all the banking malware families. 
```
Ainslot 
Ares
Banbra 
...
Vkont
Wemon
Yaludle
ZeuS
```
The `README.md` can be sorted by date, alphabetically or however is convenient. Within the `families` directory there are three types of files.

 1. `template.md` - Contains the malware template.
 2. `malware_family_X.md` - Copy of `template.md` renamed with the family of malware.
 3. `malware_family_X` - Directory renamed with the family of malware.
	 - Used for storage. 

A skeleton using Python and `template.md` can be created all of the banking families.  The following code creates the template and directory for each family and prints out the Markdown code for `README.md`.
```
import shutil
import os 
fam = """Adramax 
Ainslot 
Ares
Banbra 
Vkont
Wemon
Yaludle
ZeuS"""
for f in fam.split("\n"):
    temp = f.strip(" ").replace(" ", "_")
    name = temp + ".md"
    shutil.copy2("template.md", name)
    os.mkdir(f)
    print " - [%s](./families/%s)" % (f, name)
```
Generated Markdown Code
```
 - [Adramax ](./families/Adramax.md)
 - [Ainslot ](./families/Ainslot.md)
 - [Ares](./families/Ares.md)
 - [Banbra ](./families/Banbra.md)
 - [Vkont](./families/Vkont.md)
 - [Wemon](./families/Wemon.md)
 - [Yaludle](./families/Yaludle.md)
 - [ZeuS](./families/ZeuS.md)
```

The generated markdown output can be added to `README.md` which would generate the following example links. See [POC](./POC/README.MD) for working example. 

 - [Adramax ](./families/Adramax.md)
 - [Ainslot ](./families/Ainslot.md)
 - [Ares](./families/Ares.md)
 - [Banbra ](./families/Banbra.md)
 - [Vkont](./families/Vkont.md)
 - [Wemon](./families/Wemon.md)
 - [Yaludle](./families/Yaludle.md)
 - [ZeuS](./families/ZeuS.md) 

Each of the malware families pages would contain a template that then can be populated.  Now comes the power of community for tracking the families.

#### Closing Thoughts
Git has a lot of potential for intel tracking. I'm hoping more people adopt a similar methodology.