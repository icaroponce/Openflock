from imports import *
from handlers import *

routes = [
    (r'/',MainHandler),
    (r'/profile/.*',ProfileHandler),
    (r'/promote/.*',PromoteHandler),
    (r'/link/.*',RepoHandler),
    (r'/mypromotedrepos',MyPromotedRepos),
    (r'/redirecting/.*',GitHubView),
    (r'/edit/.*',RepoEditHandler),
    (r'/logout',LogoutHandler),
    (r'/auth_redirect',AuthRedirect),
    (r'/promote_verify',PromoteVerify),
    (r'/authorization',Authorization),
	(r'/halloffame',HallOfFame)
    ]
