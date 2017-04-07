from django.test import TestCase

from .topics import Topic, TopicList

class TopicTest(TestCase):
    def setUp(self):
        self.topic = Topic()

    def test_not_integer_upvote(self):
        self.topic = Topic()
        with self.assertRaises(ValueError):
            self.topic.upvote('not an integer')

    def test_not_integer_downvote(self):
        self.topic = Topic()
        with self.assertRaises(ValueError):
            self.topic.upvote('not an integer')
        
    def test_not_equals_vote_score(self):
        self.topic = Topic()
        self.topic.upvote(1)
        self.topic.upvote(1)
        wrong_vote_score = 3
        self.assertNotEquals(self.topic.vote_score, wrong_vote_score)

    def test_equals_vote_score(self):
        self.topic = Topic()
        self.topic.upvote(1)
        self.topic.upvote(1)
        correct_vote_score = 2
        self.assertEquals(self.topic.vote_score, correct_vote_score)

class TopicListTest(TestCase):
    def setUp(self):
        pass

    def test_invalid_length_upon_append(self):
        tl = TopicList()
        tl.append(Topic('test'))
        tl.append(Topic('another test'))
        wrong_length_count = 3
        self.assertNotEquals(tl.__len__(), wrong_length_count)

    def test_valid_length_upon_append(self):
        tl = TopicList()
        tl.append(Topic('test'))
        tl.append(Topic('another test'))
        correct_length_count = 2
        self.assertEquals(tl.__len__(), correct_length_count)

    def test_get_attr_raise_attr_error(self):
        tl = TopicList()
        tl.append(Topic('test'))
        tl.append(Topic('another test'))

        with self.assertRaises(AttributeError):
            tl.get_obj_by_attr_or_none('not_defined_attribute', 'not_defined_value')

    def test_get_attr_none(self):
        tl = TopicList()
        tl.append(Topic('test'))
        tl.append(Topic('another test'))
        self.assertIsNone(tl.get_obj_by_attr_or_none('topic_id', 'not existing id'))

    def test_get_attr_exists(self):
        tl = TopicList()
        t1 = Topic('test')
        t2 = Topic('another test')
        tl.append(t1)
        tl.append(t2)
        topic_obj = tl.get_obj_by_attr_or_none('topic_id', t1.topic_id)
        self.assertEquals(topic_obj.topic_id, t1.topic_id)
