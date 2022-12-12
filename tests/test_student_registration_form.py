import os
from selene import be, command, have
from selene.support.shared import browser

picture_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'pic', 'photo_2016-08-25_20-45-23.jpg'))


def test_registration_form():
    #заполнение формы
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Dinara')
    browser.element('#lastName').should(be.blank).type('Shurukhina')
    browser.element('#userEmail').should(be.blank).type('testEmail@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('81234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('May')
    browser.element('.react-datepicker__year-select').send_keys('1986')
    browser.element('.react-datepicker__day--014').click()
    browser.element('#subjectsInput').should(be.blank).type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(picture_path)
    browser.element('#currentAddress').type('Moscow, Tverskaya str, 19, 173')
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#react-select-3-input').send_keys('NCR').press_enter()
    browser.element('#react-select-4-input').send_keys('Delhi').press_enter()
    browser.element('#submit').click()
    #проверка результата
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text(
        'Dinara'
        and 'Shurukhina'
        and 'testEmail@gmail.com'
        and 'Female'
        and '81234567890'
        and '14 May,1986'
        and 'Computer Science'
        and 'Reading, Music'
        and 'photo_2016-08-25_20-45-23.jpg'
        and 'Moscow, Tverskaya str, 19, 173'
        and 'NCR Delhi'
    ))








