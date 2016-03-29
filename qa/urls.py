from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='qa_index'),
    url(r'^question/(?P<pk>\d+)/$',
        views.QuestionDetailView.as_view(), name='qa_detail'),
    url(r'^new-question/$', views.CreateQuestionView.as_view(),
        name='qa_create_question'),
    url(r'^answer/(?P<question_id>\d+)/$',
        views.CreateAnswerView.as_view(), name='qa_create_answer'),
    url(r'^comment/(?P<answer_id>\d+)/$',
        views.CreateCommentView.as_view(), name='qa_create_comment'),
    url(r'^vote/question/(?P<object_id>\d+)/$', views.QuestionVoteView.as_view(), name='qa_question_vote'),
    url(r'^vote/answer/(?P<object_id>\d+)/$', views.AnswerVoteView.as_view(), name='qa_answer_vote'),
    url(r'^search/$', views.search, name='qa_search'),
    url(r'^tag/(?P<tag>[-\w]+)/$', views.tag, name='qa_tag'),
    url(r'^thumb/(?P<user_id>\d+)/(?P<question_id>\d+)/(?P<op_code>\d+)/$',
        views.thumb, name='qa_thumb'),

    url(r'^profile/(?P<user_id>\d+)/$', views.profile, name='qa_profile'),
]
