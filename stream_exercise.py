

class StreamProcessor(object):
    """
    Write a stream processor class that does the following:
        1. You initialize an instance with a stream of digits
          (AKA: file-like object, instance of StringIO), and
          store it as an instance variable.
        
          eg: f = io.StringIO("234761640930110349378289194")
              my_stream_processor = MyStreamProcessor(f)
              
        2. You call a `process` method of my_stream_processor.
        
          This method:
          
            1. Reads two digits at a time from the beginning of the stream
            2. Converts the two digits into a number, and adds that number
               to a running total.
            3. Once this number reaches 200 or more, the method returns how
               many two digit numbers it had to add together to reach its
               total.
            4. If `process` reaches the end of the stream BEFORE it has
               reached a sum of 200, then it will return how many two
               digit numbers it found before reaching the end of the
               stream.
            5. The method will add AT MOST 10 of these two digit numbers
               together: if it reaches the 10th two digit number and the
               sum has not yet reached 200, then the method will stop and
               return 10.

    For example, given a stream yielding "234761640930110349378289194", the
    process method will:

            1. Read two digits at a time from the stream: "23", "47", "61", etc.
            2. Convert these digits into a number: 23, 47, 61, etc., and  make a
               running total of these numbers: 23 + 47 equals 70. 70 + 61 equals
               131, etc.
            3. For this particular stream, the running total will exceed 200 after
               5 such additions: the `process` method should return 5.

    You can see the `tests.py` file for more examples of expected outcomes.
    """

    def __init__(self, stream):
        self._stream = stream

    def process(self):
        """
        Read two-digit pairs from the provided stream and add them to a running total.
        Return the number of two-digit pairs read. Return if the running total is
        greater than or equal to 200, once the total number of digit pairs read
        reaches 10, or when the stream runs out. If the stream consists of an odd
        number of digits, the last digit is not used since it does not constitute
        a pair.
        """

        count = 0  # How many two-digit numbers the `process` method has added
                   # together.
        total = 0  # The running total of sums.

        while count < 10 and total < 200:

            digits = self._stream.read(2)
            if len(digits) < 2:
                # Return if there are fewer than two digits remaining in the stream
                return count
            total += int(digits)
            count += 1

        return count
