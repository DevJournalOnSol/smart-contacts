# feed
# Built with Seahorse v0.2.4
#

from seahorse.prelude import *

declare_id('7Hz71HGc5M44c7Q7qAtneeKgh8LbSjLHaw45fy4N2WNQ')

class Feed(Account):
  day_reset_time: i64

class Post(Account):
    owner: Pubkey
    time: i64
    content:str

@instruction
def initialize_feed(feed: Empty[Feed], user: Signer, clock: Clock):
  feed = feed.init(
    payer=user
  )
  feed.day_reset_time = clock.unix_timestamp()

@instruction
def write(feed: Feed, user: Signer, clock: Clock, content: str, post: Empty[Post]):
  seconds_passed = clock.unix_timestamp() - feed.day_reset_time
  print(seconds_passed)
  post = post.init(
    payer=user
  )
  post.owner = user.key()
  post.time = clock.unix_timestamp()
  post.content = content