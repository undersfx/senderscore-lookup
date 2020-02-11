from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = '''Command Line Tool for Lookup at Sender Score.

More information at www.senderscore.org.'''
  
setup( 
        name ='senderscore', 
        version ='0.1.0', 
        author ='Thiago "Undersfx" Rodrigues', 
        author_email ='undersoft.corp@gmail.com', 
        url ='https://github.com/undersfx/senderscore-lookup', 
        description ='Senderscore command line lookup tool', 
        long_description = long_description,
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'senderscore = senderscore.senderscore:main'
            ] 
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        keywords ='sender score lookup cli undersfx', 
        install_requires = requirements,
        zip_safe = False
)
