from django import template
from django.forms.fields import MultipleChoiceField

from copy import copy
from wagtail.core.models import Page
from molo.forms.models import (
    MoloFormPage, FormsIndexPage, PersonalisableForm)

from molo.core.templatetags.core_tags import get_pages
from django.shortcuts import get_object_or_404

register = template.Library()


def get_form_list(
        context,
        only_linked_forms=False,
        only_direct_forms=False,
        only_yourwords=False,
        personalisable_form=False):
    if only_linked_forms and only_direct_forms:
        raise ValueError('arguments "only_linked_forms" and '
                         '"only_direct_forms" cannot both be True')

    context = copy(context)
    locale_code = context.get('locale_code')
    main = context['request'].site.root_page
    page = FormsIndexPage.objects.child_of(main).live().first()
    if page:
        forms = []
        if only_linked_forms:
            forms = (MoloFormPage.objects.child_of(page).filter(
                language__is_main_language=True,
                display_form_directly=False,
                your_words_competition=False).exact_type(
                    MoloFormPage).specific())
        elif only_direct_forms:
            forms = (MoloFormPage.objects.child_of(page).filter(
                language__is_main_language=True, display_form_directly=True,
                your_words_competition=False).exact_type(
                    MoloFormPage).specific())
        elif only_yourwords:
            forms = (MoloFormPage.objects.child_of(page).filter(
                language__is_main_language=True,
                your_words_competition=True).exact_type(
                    MoloFormPage).specific())
        elif personalisable_form:
            forms = (PersonalisableForm.objects.child_of(page).filter(
                language__is_main_language=True).exact_type(
                    PersonalisableForm).specific())
        else:
            forms = (MoloFormPage.objects.child_of(page).filter(
                language__is_main_language=True).exact_type(
                    MoloFormPage).specific())
    else:
        forms = MoloFormPage.objects.none()
    context.update({
        'forms': get_pages(context, forms, locale_code)
    })
    return context


def add_form_objects_to_forms(context):
    forms = []
    for form_page in context['forms']:
        form = None
        if (form_page.allow_multiple_submissions_per_user or
                not form_page.has_user_submitted_form(
                    context['request'], form_page.id)):
            form = form_page.get_form()

        forms.append({
            'molo_form_page': form_page,
            'form': form,
        })

    context.update({
        'forms': forms,
    })

    return context


@register.inclusion_tag('forms/forms_headline.html', takes_context=True)
def forms_list_headline(context):
    return get_form_list(context)


@register.inclusion_tag('forms/forms_list.html', takes_context=True)
def forms_list(
        context, pk=None, only_linked_forms=False,
        only_direct_forms=False, only_yourwords=False,
        personalisable_form=False):
    context = get_form_list(
        context,
        only_linked_forms=only_linked_forms,
        only_direct_forms=only_direct_forms,
        only_yourwords=only_yourwords,
        personalisable_form=personalisable_form)
    return add_form_objects_to_forms(context)


@register.simple_tag(takes_context=True)
def load_user_choice_poll_form(context, form, field, choice):
    if not form or not field:
        return False
    request = context['request']
    form = form.specific.get_main_language_page()
    SubmissionClass = form.specific.get_submission_class()
    submissions = SubmissionClass.objects.filter(
        page=form, user=request.user)
    if not submissions.exists():
        return False
    for submission in submissions:
        data = submission.get_data()
        if field in data and data[field] == choice:
            return True
    return False


@register.simple_tag(takes_context=True)
def submission_has_article(context, form_id, submission_id):
    form_page = get_object_or_404(Page, id=form_id).specific
    SubmissionClass = form_page.get_submission_class()
    submission = SubmissionClass.objects.filter(
        page=form_page).filter(pk=submission_id).first()
    if submission.article_page is None:
        return False
    return True


@register.inclusion_tag('forms/forms_list.html', takes_context=True)
def forms_list_for_pages(context, pk=None, page=None):
    context = copy(context)
    locale_code = context.get('locale_code')
    if page:
        forms = (
            MoloFormPage.objects.child_of(page).filter(
                language__is_main_language=True).specific())
    else:
        forms = MoloFormPage.objects.none()

    context.update({
        'forms': get_pages(context, forms, locale_code)
    })
    return add_form_objects_to_forms(context)


@register.filter(name='is_multiple_choice_field')
def is_multiple_choice_field(value):
    return isinstance(value.field, MultipleChoiceField)
