#### General

##### Check the Repo Content

Files that must be inside the repository:

- Detailed documentation in the `README.md` file.
- Source code for the Image Inspector tool.
- Any required configuration files and scripts for running the tool.

###### Are all the required files present?

##### Play the Role of a Stakeholder

Organize a simulated scenario where the student takes on the role of a **Digital Forensics Expert** and explains their solution and knowledge to a team or stakeholder. Evaluate their grasp of the concepts and technologies used in the project, their communication efficacy, and their critical thinking about their solution and the knowledge behind this project.

Suggested role-play questions include:

- What is metadata in the context of digital images, and why is it important?
- How does steganography work, and what are its potential uses and risks?
- What challenges did you face while developing the Image Inspector tool, and how did you address them?
- How can this tool be used in real-life digital forensics or cybersecurity scenarios?
- What ethical considerations should be taken into account when analyzing images for hidden data?

###### Was the student able to answer all the questions?

###### Did the student demonstrate a thorough understanding of the concepts and technologies used in the project?

###### Was the student able to communicate effectively, justify their decisions, and explain the knowledge behind this project?

###### Was the student able to evaluate the value of this project in real-life scenarios?

###### Did the student demonstrate an understanding of ethical and legal considerations related to digital forensics?

##### Check the Student Documentation in the `README.md` File

###### Does the `README.md` file contain all the necessary information about the tool (prerequisites, setup, configuration, usage, etc.)?

###### Does the `README.md` file contain clear guidelines and warnings about the ethical and legal use of the tool?

##### Review the Tool's Design and Implementation

1. **Help Command:**

```sh
$> image-inspector --help
```

###### Does the output include an explanation of how to use the tool, with all options clearly described?

2. **Metadata Extraction Option:**

```sh
$> image-inspector -m -o metadata.txt image-example1.jpeg
```

###### Does the output correctly extract and display metadata such as geolocation, device information, and date/time?

###### Is the output stored in the file specified in the output parameter?

3. **Steganography Detection Option:**

```sh
$> image-inspector -s -o hidden_data.txt image-example1.jpeg
```

###### Does the output correctly detect and extract hidden data (such as a PGP key block starting with `-----BEGIN PGP PUBLIC KEY BLOCK-----`)?

###### Is the output stored in the file specified in the output parameter?

4. **Combined Options:**

```sh
$> image-inspector -m -s -o results.txt image-example1.jpeg
```

###### Can the tool run both -m and -s in a single command, saving both results to the specified output file correctly?

##### Testing with Images

You will be provided with example images to test the student's tool. Feel free to test with other images as well.

The example images are attached:

- [image-example1.jpeg](resources/image-example1.jpeg)
- [image-example2.jpeg](resources/image-example2.jpeg)
- [image-example3.jpeg](resources/image-example3.jpeg)
- [image-example4.jpeg](resources/image-example4.jpeg)

###### Test the tool with the provided example images to ensure the tool's robustness.

###### Does the tool successfully extract hidden data from the test images?

###### Does the tool produce consistent and reliable results across different images?

##### Error Handling

Test the tool with an image that has no metadata and no hidden data.

###### Does the tool gracefully handle an image that has no metadata and no hidden PGP key (no crashes, clear message to user)?

##### Ensure That the Student Submission Meets the Project Requirements

1. **Functionality:** Does the tool correctly extract metadata and detect hidden data using steganography?

2. **Data Accuracy:** Is the extracted information accurate and properly formatted?

3. **Ethical Considerations:** Are there clear guidelines and warnings about the ethical and legal use of the tool?

4. **Usability:** Is the tool user-friendly and well-documented?

###### Did the tool design and implementation align with all the project requirements above?

###### Was the student able to implement a functional and reliable tool that meets the project requirements?

#### Bonus

###### + Did the student implement additional steganography detection methods beyond LSB?

###### + Did the student implement a graphical user interface (GUI)?

###### + Is this project an outstanding project that exceeds the basic requirements?
