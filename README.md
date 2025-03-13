# Echo Server with Wireshark Analysis

## **Project Overview**
This project involves building a simple Echo Server using Python's `socket` module. The server listens for incoming connections and processes client messages based on a set of predefined rules.

## **Features**
1. **Echo Server**: The server receives a single line of input from the client and responds according to the first character:
   - If the message starts with `A`, the server returns the rest of the message in **lowercase**.
   - If the message starts with `D`, the server returns the rest of the message in **reverse order**.
   - If the message starts with `C`, the server returns the entire message **in uppercase**.
   - If the first character is anything else, the server returns the same message unmodified.

## **Prerequisites**
Before running the echo server, make sure you have:
1. **Python 3.x** installed on your system.
2. **Wireshark** installed and ready to capture network traffic.
3. **Basic knowledge of Python sockets.**

## **How to Run the Server and Client**
1️⃣ **Start the server**:
   ```sh
   python echo_server.py
   ```

2️⃣ **Start Wireshark capture**:
   - Open Wireshark and select the appropriate network adapter. If the client and server run on the same machine, choose `Adapter for loopback traffic capture`.
   - In the filter bar, enter:
     ```
     tcp.port == 12345
     ```
   - Click **Start** to begin capturing traffic.

3️⃣ **Run the Client**
   - Open another terminal and run:
     ```
     python echo_client.py
     ```
   - Once the client is running, enter the following messages (one per line):
     ```
     Ahello
     Dworld
     Cpython
     ```
   - The expected responses from the server will be:
     ```
     hello
     dlrow
     PYTHON
     ```

4️⃣ **Stop Wireshark and Save the Capture**
   - After running the client, go back to Wireshark.
   - Stop the capture and apply the filter:  
     ```
     tcp.port == 12345
     ```
   - Save the capture as a `.pcapng` file.

## **File Submission**
When submitting, include the following:
1. **`echo_server.py`** (Python script for the echo server).
2. **`echo_client.py`**: The client script that sends messages to the server.
3. **`Wireshark_Capture.pcapng`**: The captured Wireshark traffic file.
4. **This README.md**: Explaining the project setup, how to run it, and how to analyze the captured Wireshark traffic.

---
  
If you need help refining this README or adding screenshots, let me know! 🚀      
