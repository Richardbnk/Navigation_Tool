import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='navigation_tool',
    version='1.0.0',
    author="Richard Raphael Banak",
    description="Tool to assist navigation using mouse and keyboard for automated actions when RPA techniques are not effective.",
    url="https://github.com/Richardbnk/navigation_tool",
    packages=['navigation_tool'],
    
    py_modules = ['pyautogui'],
    
    
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[required],
)
