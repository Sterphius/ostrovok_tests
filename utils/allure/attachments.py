import allure
from allure_commons.types import AttachmentType
from selene import browser

from utils.browserstack import get


def add_screen_xml_dump(*, name=None):
    allure.attach(
        browser.driver.page_source,
        name=name or 'page xml dump',
        attachment_type=allure.attachment_type.XML,
    )


def video_from_browserstack(session_id, *, name='video recording'):
    video_url = get.video_url(session_id=session_id)

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name=name,
        attachment_type=allure.attachment_type.HTML,
    )


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png',
    )


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(
        body=log,
        name='browser_logs',
        attachment_type=AttachmentType.TEXT,
        extension='.log',
    )


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(
        body=html,
        name='page_source',
        attachment_type=AttachmentType.HTML,
        extension='.html',
    )


def add_video(browser):
    video_url = (
            "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    )
    html = (
            "<html><body><video width='100%' height='100%' controls autoplay><source src='"
            + video_url
            + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        body=html,
        name='video_' + browser.driver.session_id,
        attachment_type=AttachmentType.HTML,
        extension='.html',
    )
