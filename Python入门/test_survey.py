# from survey import AnonymousSurvey
#
# def test_store_single_response():
#     """测试单个结果可以正常保存"""
#     question = "What language did you first learn?"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses
#
# def test_store_three_response():
#     """测试三个结果可以正常保存"""
#     question = "What language did you first learn?"
#     language_survey = AnonymousSurvey(question)
#     responses = ['Chinese', 'English', 'French']
#     for response in responses:
#         language_survey.store_response(response)
#     for response in responses:
#         assert response in language_survey.responses

###     上面的测试单元太麻烦了，每次都需要重新生成一个类的实例，下面使用装饰器来创建一个实例
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的实例"""
    question = "What language did you first learn?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """测试单个结果可以正常保存"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    """测试三个结果可以正常保存"""
    responses = ['Chinese', 'English', 'French']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
