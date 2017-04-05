
class Topic(object):
    def __init__(self, topic=None, vote_count=0):
        self.topic = topic
        self.vote_count = vote_count

    @staticmethod
    def validate_positive_integer(value):
	try:
            value = int(value)
            if value < 1:
                raise ValueError("{} is not a positive integer".format(value))
        except (ValueError, TypeError):
            raise ValueError("{} is not a valid integer".format(value))

        return value


    def upvote(self, count):
        """
            This method is simply incrementing the vote. 
            Validates the parameter 'count' that it must be positive integer only.
        """
        count = self.validate_positive_integer(count)

        self.vote_count = self.vote_count + count
        return self.vote_count

    def downvote(self, count):
        """
            This method is simply decrementing the vote. 
            Validates the parameter 'count' that it must be positive integer only.
        """
        count = self.validate_positive_integer(count)

        self.vote_count = self.vote_count - count
        return self.vote_count

    @property
    def total_vote_count(self):
        """
            Simply returning the total vote . 
        """
        return self.vote_count
