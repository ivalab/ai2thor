# Unity Development

This README only provides instructions for those who'd like to comple and build AI2THOR on local. It is only tested on Ubuntu 18.04. If you wish to make changes to the Unity scenes/assets or change any source codes, you will need three steps: firstly install Unity Hub, then install Unity Editor with specific version and lastly compile and build the source code.

## Step 1
Follow the [instructions](https://docs.unity3d.com/Manual/GettingStartedInstallingHub.html) provided in the official website.

## Step 2
We will need specific version of Unity Editor, which depends on which version of AI2THOR you are using. In my case, Unity Editor 2019.4.20 is needed. All supported versions can be found [here](https://unity3d.com/get-unity/download/archive). If you are lucky, you might be able to click the green icon of unity hub, which will invoke your installed Unity Hub. If nothings happen after you click it, you can instead launch Unity Hub with the link of the Unity Editor you want. In my case, run
```
./UnityHub.AppImage unityhub://2019.4.20f1/6dd1c08eedfa
```

## Step 3
There are two ways to build local builds. Two different way will lead to different ways of initializing controllers. 

### Method 1
Follow the way provided in the AI2THOR. To complie and build the soruce code, run the following commands under the ai2thor base directory
```python
pip install invoke
invoke local-build --arch=Linux64
```
This will create a build beneath the directory 'unity/builds/thor-Linux64-local'. To use this build in your code, make the following change:

```python
controller = ai2thor.controller.Controller(
    local_executable_path="<BASE_DIR>/unity/builds/thor-Linux64-local/thor-Linux64-local"
)
```

### Method 2
Just build for Linux in the Unity Editor, which will give you more error information when your modified code still has some bugs. 
```
1. Launch the Unity Hub and find the AI2THOR project under 'Projects'
2. Click the project to open it
3. Go to file/build settings and click Build.
4. Choose one directionary for saving built file and don't forget to provide the name, e.g., build_file._x86_64
5. Initialize the controller via controller = ai2thor.controller.Controller(
    local_executable_path="<BASE_DIR>/unity/builds/build_file._x86_64"
```
