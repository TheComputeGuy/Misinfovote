from dotenv import load_dotenv
from os import environ as env
from pymongo import MongoClient

load_dotenv()

# Connect to the MongoDB database
client = MongoClient(f'mongodb://{env.get('DB_USER')}:{env.get('DB_PASSWORD')}@{env.get('DB_ENDPOINT')}')
db = client[f'{env.get('DB_NAME')}']

# Method to insert data into the post collection
def insertPost(postID, modPred, userID, votesTrusted, avgTrusted, votesUntrusted, avgUntrusted):
    db.posts.insert_one({
        'postID': postID,
        'userID': userID,
        'modPred': modPred,
        'votesTrusted': votesTrusted,
        'avgTrusted': avgTrusted,
        'votesUntrusted': votesUntrusted,
        'avgUntrusted': avgUntrusted
    })

# Method to update the trust stats of a post
def updatePostTrusted(postID, votesTrusted, avgTrusted):
    db.posts.update_one(
        {'postID': postID},
        {'$set': {
            'votesTrusted': votesTrusted,
            'avgTrusted': avgTrusted
            }
        }
    )

# Method to update the untrusted stats of a post
def updatePostUntrusted(postID, votesUntrusted, avgUntrusted):
    db.posts.update_one(
        {'postID': postID},
        {'$set': {
            'votesUntrusted': votesUntrusted,
            'avgUntrusted': avgUntrusted
            }
        }
    )

# Method to delete a post from the collection
def deletePost(postID):
    db.posts.delete_one({'postID': postID})

# Method to get a post by ID
def getPost(postID):
    return db.posts.find_one({'postID': postID})

# Method to insert user into the Users collection
def insertUser(userID, isTrustedUser):
    db.users.insert_one({
        'userID': userID,
        'isTrustedUser': isTrustedUser
    })

# Method to trust score the votes of a user
def updateUser(userID, isTrustedUser):
    db.users.update_one(
        {'userID': userID},
        {'$set': {
            'isTrustedUser': isTrustedUser
            }
        }
    )

# Method to delete a user from the collection
def deleteUser(userID):
    db.users.delete_one({'userID': userID})

# Method to get a user by ID
def getUser(userID):
    return db.users.find_one({'userID': userID})

# Get multiple users
def getUsers(userIDs):
    return list(db.users.find({'userID': {'$in': userIDs}}))

# Method to add a vote into the votes collection
def insertVote(userID, vote, postID):
    db.votes.insert_one({
        'user': userID,
        'vote': vote,
        'postID': postID
    })

# Method to update a vote in the votes collection
def updateVote(userID, postID, vote):
    db.votes.update_one(
        {'user': userID, 'postID': postID},
        {'$set': {'vote': vote}}
    )

# Method to delete a vote from the collection
def deleteVote(userID, postID):
    db.votes.delete_one({'user': userID, 'postID': postID})

# Method to get a vote by user and post
def getVote(userID, postID):
    return db.votes.find_one({'user': userID, 'postID': postID})

# Method to get all votes by user
def getVotesByUser(userID):
    return list(db.votes.find({'user': userID}))

# Method to get all votes by post
def getVotesByPost(postID):
    return list(db.votes.find({'post ID': postID}))
