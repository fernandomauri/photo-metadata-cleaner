# Image Metadata Cleaner

## Overview
There have been some cases where seemingly innocuous images posted on the Internet have led to grave consequences. [One such case](https://www.army.mil/article/75165/geotagging_poses_security_risks) involved the location of an aviation compound being revealed and then attacked by adversaries after soldiers posted images from inside on social media. The location of the compound was revealed due to the EXIF (Exchangeable Image File Format) data embedded in each photo: Camera information and settings, image information, latitude and longitude, and more. Fortunately, no human lives were lost. In another case, antivirus tycoon John McAfee was a fugitive of the law in Belize and hid in Guatemala. His exact location was exposed via EXIF data when a journalist posted a photo with the two of them, which led to his arrest shortly after:


<div align="center">
  <img alt="John McAfee with a reporter in Guatemala" src=https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2012/12/2012-12-03_13h11_54.jpg width=75%>
</div>


Both of these cases serve as a lesson that security is essential in our increasingly digital world, even for what might seem minuscule.

## Purpose
Cleans photos given by the user of their EXIF data. This program was inspired by some of my work at a high profile digital media company where privacy and security is a business-critical priority. This simple program will place the scrubbed duplicates into the same directory as the original, and has the added benefit of a (slightly) decreased file size. 

## Prerequisites
This program requires Docker to be installed on your machine. Instructions for installation specific to your machine can be found [here](https://docs.docker.com/get-started/get-docker/).

## Dependencies
- Docker
- Python 3
- Pillow

## Instructions
1. Once the repo is cloned and Docker is installed, change your working directory in your terminal to this app. A default picture for us to scrub will be located in the <i>/app/images folder</i>, and if you'd like to use your own, I would suggest adding those to <i>/app/images</i>. 
2. Run the command in `docker build -t metadata_cleaner .` to build a Docker image. You could replace the `metadata_cleaner` tag with anything of your choosing if preferred.
3. Create a container from the new Docker image by running `docker run -d metadata_cleaner`.
If you'd like to give the container a chosen name upon creation, you can add the `--name your-container-name` option to the above command after `-d`.
4. After the container is created and started, it runs our Python program to produce scrubbed images. Because of the stateless nature of containers as well as their behavior of stopping after their processes are run, we want to make sure we keep our new container running.
5. Check for your brand new container and ensure it's running with `docker ps`. It won't show up if it's not running, but we can verify that it was created with `docker ps -a`.
6. Our container is running in "detached" mode (the `-d` in our `docker run` command) so we can interact with it while letting it do its thing in the background. We want to enter the container to see if the scrubbed images were produced and saved. We will do so with `docker exec -ti your-container-name /bin/bash`. You should now be inside your container in the app's directory.
7. Check for the scrubbed copy of your original image with the command `ls /app/images`. The scrubbed image should have the same name as the original with <i>"-SCRUBBED"</i> appended before the file extension.

## Results
You should be able to check and compare the metadata between the two images and notice that the scrubbed copy is slightly smaller in file size and reveals less EXIF metadata. I'll include an example below:

<img width="669" height="562" alt="EXIF before and after" src="https://github.com/user-attachments/assets/82b89f8a-746a-4328-8b5b-0779541a5658" />

My original image to the left has extensive details, including the device I used as well as the settings enabled to take the picture. What might be considered the most sensitive information revealed here is my exact latitude and longitude, which would place me at <a href="https://maps.app.goo.gl/4VFfBHoutaNwaoXL8">Paul Smith's Pink Wall</a> on Melrose.*

On the right, we can see that the original data associated with my picture is no longer there, so our program succeeded!

###### <i>*If you're ever in that vicinity, I highly encourage you to try the panko-battered onion rings at <a href="https://www.latimes.com/food/story/2025-03-13/nipsey-hussles-legacy-lives-on-with-marathon-burger-a-new-melrose-diner">Marathon Burger</a></i>

### Note
There may or may not be added features to this in the future, but I wanted to make sure this at least worked first.

