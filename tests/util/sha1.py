import hashlib


class Sha1:

    @staticmethod
    def get_hexa_string(file: str):
        block_size = 65536  # The size of each read from the file

        file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file, 'rb') as f:  # Open the file to read it's bytes
            fb = f.read(block_size)  # Read from the file. Take in the amount declared above
            while len(fb) > 0:  # While there is still data being read from the file
                file_hash.update(fb)  # Update the hash
                fb = f.read(block_size)  # Read the next block from the file

        return file_hash.hexdigest()  # Get the hexadecimal digest of the hash