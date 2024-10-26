import random, time
from .other import domain, save
from requests.exceptions import JSONDecodeError

class Interactions:
    # login using session
    def __init__(self, ses) -> None:
        self.ses = ses
        self.reaction_type = ['like', 'love', 'haha', 'angry']

    # React to a post using the post id 
    # INFO: If you do not choose a reaction then it will be chosen randomly.
    def reactions(self, post_id: str, reactions: str=None) -> dict:
        react_fixed = reactions or random.choice(self.reaction_type)
        data = {'do': 'react_post', 'id': str(post_id).replace(domain('posts/'), ''), 'reaction': react_fixed}
        try:
            self.ses.post(domain('includes/ajax/posts/reaction.php'), data=data).json()
            return {'status': 'success', 'data':{'url': domain('posts/'+ str(post_id)), 'post_id': str(post_id), 'reaction': react_fixed, 'time': time.ctime()}}
        except JSONDecodeError:
            return {'status': 'faillure', 'data': None}

    # share post
    # INFO: Share to timeline if group id is empty
    def share(self, post_id: str, caption: str=None, group_id: str=None) -> dict:
        params = {'do': 'create', 'post_id': str(post_id)}
        create = self.ses.get(domain('includes/ajax/posts/share.php'), params=params).json()

        params = {'do': 'publish', 'post_id': str(post_id)}
        data = {'share_to': 'timeline' if group_id is None else 'group', 'group_id': str(group_id), 'message': caption}
        
        try:
            output = self.ses.post(domain('includes/ajax/posts/share.php'), params=params, data=data).json()
            if '#modal-success' in str(output):
                return {'status': 'success', 'data':{'to': data['share_to'], 'caption': caption, 'time': time.ctime(), 'target': domain('posts/'+ str(post_id))}}
        except JSONDecodeError:
            pass

        return {'status': 'faillure', 'data': None}

    # comment post
    # WARN: can't use attachments yet
    def comment(self, post_id: str, text: str) -> dict:
        data = {'handle': 'post', 'id': str(post_id), 'message': str(text)}

        try:
            output = self.ses.post(domain('includes/ajax/posts/comment.php'), data=data).json()
            if 'comment' in str(output):
                return {'status': 'success', 'data':{'url': domain('posts/'+ str(post_id)), 'post_id': str(post_id), 'text': str(text), 'time': time.ctime()}}
        except JSONDecodeError:
            pass

        return {'status': 'faillure', 'data': None}

    # join group
    # WARN: haven't found a way to find group id yet
    def join_group(self, group_id: str) -> dict:
        data = {'do': 'group-join', 'id': str(group_id)}

        try:
            output = self.ses.post(domain('includes/ajax/users/connect.php'), data=data).json()
            return {'status': 'success', 'data':{'group_id': str(group_id)}}
        except JSONDecodeError:
            pass

        return {'status': 'faillure', 'data': None}
