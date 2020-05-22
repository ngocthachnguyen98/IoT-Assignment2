import unittest
import socket

import threading

from werkzeug.debug import console

PORT = 65000
# change the host if needed
HOST = ""
ADDRESS = (HOST, PORT)


# make a test server


# print "[+] Listening on %s:%d" % (ADDRESS)


class MyTestCase(unittest.TestCase):

    def run_dummy_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print("Connected to {}".format(addr))
            while True:
                # Receive message and check if it's empty
                message = conn.recv(4096)  # 4096 is the buffersize
                if (not message):
                    break

                print("Received {} bytes of data decoded to: '{}'".format(len(message),
                                                                          message.decode()))

    def testConect(self):
        # Start test server in background thread
        server_thread = threading.Thread(target=self.run_dummy_server)
        server_thread.start()
        print(console)

        import client_TCP



        server_thread.join()
    # send dummy message from a test client to the server
    # def test_1(self):
    #     client_TCP.send('testmessage'.encode())
    #     self.assertEqual(dummyServer.recv(1024).decode(), 'testmessage')
    #
    # def test_login(self):
    #     client_TCP.credentialsCheck()
    #
    # def test_unlock(self):
    #
    # def test_lock(self):
    #
    #
    # # tear down the dummy server once the test is done
    # def tearDown(self):
    #     dummyServer.close()
    #


# print the file in mp (check if received)


# send the crendentials back to ap


# test if the connection function between AP and MP is working

# test for if the validation process will break if not enough credential is provided

# test for the login function

# test if the function disconnect correctly when validation complete

if __name__ == '__main__':
    unittest.main()
