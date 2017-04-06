import uuid 

class Topic(object):
    def __init__(self, topic=None, vote_score=0):
        self.topic_id = str(uuid.uuid4())[:32].replace('-', '').lower()
        self.topic = topic
        self.vote_score = vote_score

    def __repr__(self):
        return str(self.topic)

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

        self.vote_score = self.vote_score + count
        return self.vote_score

    def downvote(self, count):
        """
            This method is simply decrementing the vote. 
            Validates the parameter 'count' that it must be positive integer only.
        """
        count = self.validate_positive_integer(count)

        self.vote_score = self.vote_score - count
        return self.vote_score

    @property
    def total_vote_score(self):
        """
            Simply returning the total vote . 
        """
        return self.vote_score

