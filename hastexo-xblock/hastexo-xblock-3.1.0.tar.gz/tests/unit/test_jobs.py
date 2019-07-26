from mock import patch, call
from django.test import TestCase
from django.utils import timezone

from hastexo.jobs import SuspenderJob, ReaperJob
from hastexo.models import Stack, StackLog
from hastexo.provider import ProviderException
from hastexo.common import (CREATE_STATE, SUSPEND_ISSUED_STATE, DELETE_STATE,
                            DELETED_STATE, SUSPEND_RETRY_STATE,
                            DELETE_IN_PROGRESS_STATE, DELETE_FAILED_STATE)


class TestHastexoJobs(TestCase):
    def setUp(self):
        self.stack_states = {
            'CREATE_IN_PROGRESS',
            'CREATE_FAILED',
            'CREATE_COMPLETE',
            'SUSPEND_IN_PROGRESS',
            'SUSPEND_FAILED',
            'SUSPEND_COMPLETE',
            'RESUME_IN_PROGRESS',
            'RESUME_FAILED',
            'RESUME_COMPLETE',
            'DELETE_IN_PROGRESS',
            'DELETE_FAILED',
            'DELETE_COMPLETE'}

        # Create a set of mock stacks to be returned by the mock provider.
        self.stacks = {}
        for state in self.stack_states:
            stack = {"status": state,
                     "outputs": {"bogus": "value"}}
            self.stacks[state] = stack

        # Mock settings
        self.settings = {
            "suspend_timeout": 120,
            "suspend_concurrency": 1,
            "suspend_in_parallel": False,
            "delete_age": 14,
            "delete_attempts": 3,
            "task_timeouts": {
                "sleep": 0,
                "retries": 10
            }
        }
        self.student_id = 'bogus_student_id'
        self.course_id = 'bogus_course_id'
        self.stack_name = 'bogus_stack_name'

        # Patchers
        patchers = {
            "Provider": patch("hastexo.jobs.Provider"),
        }
        self.mocks = {}
        for mock_name, patcher in patchers.items():
            self.mocks[mock_name] = patcher.start()
            self.addCleanup(patcher.stop)

    def test_dont_suspend_stack_with_no_provider(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'RESUME_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [self.stacks[state]]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_not_called()
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, state)

    def test_suspend_stack_for_the_first_time(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'CREATE_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [self.stacks[state]]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_called_with(self.stack_name)
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, SUSPEND_ISSUED_STATE)

    def test_suspend_stack_for_the_second_time(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'RESUME_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [self.stacks[state]]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_called_with(self.stack_name)
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, SUSPEND_ISSUED_STATE)

    def test_dont_suspend_unexistent_stack(self):
        # Setup
        mock_provider = self.mocks["Provider"].init.return_value

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_not_called()

    def test_dont_suspend_live_stack(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout - 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'CREATE_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [self.stacks[state]]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_not_called()
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, state)

    def test_dont_suspend_failed_stack(self):
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'RESUME_FAILED'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [self.stacks[state]]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_not_called()
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, state)

    def test_dont_suspend_suspended_stack(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'SUSPEND_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [self.stacks[state]]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_not_called()
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, state)

    def test_dont_suspend_deleted_stack(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'RESUME_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks[DELETED_STATE]
        ]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_not_called()
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, DELETED_STATE)

    def test_retry_suspending_stack(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'RESUME_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks['SUSPEND_IN_PROGRESS']
        ]

        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_not_called()
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, SUSPEND_RETRY_STATE)

    def test_retry_on_exception(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'RESUME_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [self.stacks[state]]
        mock_provider.suspend_stack.side_effect = [ProviderException("")]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, SUSPEND_RETRY_STATE)

    def test_dont_retry_failed_stack(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'RESUME_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks['RESUME_FAILED']
        ]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_not_called()
        stack = Stack.objects.get(name=self.stack_name)
        self.assertNotEqual(stack.status, SUSPEND_RETRY_STATE)

    def test_retry_suspend_failed_stack(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'SUSPEND_FAILED'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            name=self.stack_name,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks['SUSPEND_FAILED']
        ]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_called_with(self.stack_name)
        stack = Stack.objects.get(name=self.stack_name)
        self.assertEqual(stack.status, SUSPEND_ISSUED_STATE)

    def test_suspend_concurrency(self):
        # Setup
        self.settings["suspend_concurrency"] = 2
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'CREATE_COMPLETE'
        stack1_name = 'bogus_stack_1'
        stack1 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack1_name,
            suspend_timestamp=suspend_timestamp,
            provider='provider1',
            status=state
        )
        stack1.save()
        stack2_name = 'bogus_stack_2'
        stack2 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack2_name,
            suspend_timestamp=suspend_timestamp,
            provider='provider2',
            status=state
        )
        stack2.save()
        stack3_name = 'bogus_stack_3'
        stack3 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack3_name,
            suspend_timestamp=suspend_timestamp,
            provider='provider3',
            status=state
        )
        stack3.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks[state],
            self.stacks[state]
        ]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        mock_provider.suspend_stack.assert_has_calls([
            call(stack1_name),
            call(stack2_name)
        ])
        self.assertNotIn(
            call(stack_id=stack3_name),
            mock_provider.suspend_stack.mock_calls
        )
        stack1 = Stack.objects.get(name=stack1_name)
        self.assertEqual(stack1.status, SUSPEND_ISSUED_STATE)
        stack2 = Stack.objects.get(name=stack2_name)
        self.assertEqual(stack2.status, SUSPEND_ISSUED_STATE)
        stack3 = Stack.objects.get(name=stack3_name)
        self.assertEqual(stack3.status, state)

    def test_delete_old_stacks(self):
        # Setup
        delete_age = self.settings.get("delete_age")
        delete_delta = timezone.timedelta(days=(delete_age + 1))
        delete_timestamp = timezone.now() - delete_delta
        dont_delete_delta = timezone.timedelta(days=(delete_age - 1))
        dont_delete_timestamp = timezone.now() - dont_delete_delta
        state = 'RESUME_COMPLETE'
        stack1_name = 'bogus_stack_1'
        stack1 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack1_name,
            suspend_timestamp=delete_timestamp,
            provider='provider1',
            status=state
        )
        stack1.save()
        stack2_name = 'bogus_stack_2'
        stack2 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack2_name,
            suspend_timestamp=delete_timestamp,
            provider='provider2',
            status=state
        )
        stack2.save()
        stack3_name = 'bogus_stack_3'
        stack3 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack3_name,
            suspend_timestamp=dont_delete_timestamp,
            provider='provider3',
            status=state
        )
        stack3.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks[state],
            self.stacks[DELETE_IN_PROGRESS_STATE],
            self.stacks[DELETED_STATE],
            self.stacks[state],
            self.stacks[DELETE_IN_PROGRESS_STATE],
            self.stacks[DELETED_STATE],
        ]

        # Run
        job = ReaperJob(self.settings)
        job.run()

        # Assert
        mock_provider.delete_stack.assert_has_calls([
            call(stack1_name, False),
            call(stack2_name, False)
        ])
        self.assertNotIn(
            call(stack_id=stack3_name),
            mock_provider.delete_stack.mock_calls
        )
        stack1 = Stack.objects.get(name=stack1_name)
        self.assertEqual(stack1.status, DELETED_STATE)
        stack2 = Stack.objects.get(name=stack2_name)
        self.assertEqual(stack2.status, DELETED_STATE)
        stack3 = Stack.objects.get(name=stack3_name)
        self.assertEqual(stack3.status, state)

    def test_delete_exception_doesnt_hold_up_the_queue(self):
        # Setup
        delete_age = self.settings.get("delete_age")
        delete_delta = timezone.timedelta(days=(delete_age + 1))
        delete_timestamp = timezone.now() - delete_delta
        state = 'RESUME_COMPLETE'
        stack1_name = 'bogus_stack_1'
        stack1 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack1_name,
            suspend_timestamp=delete_timestamp,
            provider='provider1',
            status=state
        )
        stack1.save()
        stack2_name = 'bogus_stack_2'
        stack2 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack2_name,
            suspend_timestamp=delete_timestamp,
            provider='provider2',
            status=state
        )
        stack2.save()
        stack3_name = 'bogus_stack_3'
        stack3 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack3_name,
            suspend_timestamp=delete_timestamp,
            provider='provider3',
            status=state
        )
        stack3.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks[state],
            self.stacks[DELETE_IN_PROGRESS_STATE],
            self.stacks[DELETED_STATE],
            self.stacks[state],
            self.stacks[state],
            self.stacks[DELETE_IN_PROGRESS_STATE],
            self.stacks[DELETED_STATE],
        ]
        mock_provider.delete_stack.side_effect = [
            True,
            ProviderException(""),
            True
        ]

        # Run
        job = ReaperJob(self.settings)
        job.run()

        # Assert
        mock_provider.delete_stack.assert_has_calls([
            call(stack1_name, False),
            call(stack2_name, False),
            call(stack3_name, False)
        ])
        stack1 = Stack.objects.get(name=stack1_name)
        self.assertEqual(stack1.status, DELETED_STATE)
        stack2 = Stack.objects.get(name=stack2_name)
        self.assertEqual(stack2.status, state)
        stack3 = Stack.objects.get(name=stack3_name)
        self.assertEqual(stack3.status, DELETED_STATE)

    def test_dont_try_to_delete_certain_stack_states(self):
        # Setup
        delete_age = self.settings.get("delete_age")
        delete_delta = timezone.timedelta(days=(delete_age + 1))
        delete_timestamp = timezone.now() - delete_delta
        stack1_name = 'bogus_stack_1'
        stack1 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack1_name,
            suspend_timestamp=delete_timestamp,
            provider='provider1',
            status=DELETE_STATE
        )
        stack1.save()
        stack2_name = 'bogus_stack_2'
        stack2 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack2_name,
            suspend_timestamp=delete_timestamp,
            provider='provider2',
            status=DELETE_IN_PROGRESS_STATE
        )
        stack2.save()
        stack3_name = 'bogus_stack_3'
        stack3 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack3_name,
            suspend_timestamp=delete_timestamp,
            provider='provider3',
            status=DELETED_STATE
        )
        stack3.save()
        stack4_name = 'bogus_stack_4'
        stack4 = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack4_name,
            suspend_timestamp=delete_timestamp,
            status='CREATE_FAILED'
        )
        stack4.save()
        mock_provider = self.mocks["Provider"].init.return_value

        # Run
        job = ReaperJob(self.settings)
        job.run()

        # Assert
        mock_provider.delete_stack.assert_not_called()
        stack1 = Stack.objects.get(name=stack1_name)
        self.assertEqual(stack1.status, DELETE_STATE)
        stack2 = Stack.objects.get(name=stack2_name)
        self.assertEqual(stack2.status, DELETE_IN_PROGRESS_STATE)
        stack3 = Stack.objects.get(name=stack3_name)
        self.assertEqual(stack3.status, DELETED_STATE)
        stack4 = Stack.objects.get(name=stack4_name)
        self.assertEqual(stack4.status, 'CREATE_FAILED')

    def test_dont_wait_forever_for_deletion(self):
        # Setup
        delete_age = self.settings.get("delete_age")
        delete_delta = timezone.timedelta(days=(delete_age + 1))
        delete_timestamp = timezone.now() - delete_delta
        state = 'RESUME_COMPLETE'
        stack_name = 'bogus_stack'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack_name,
            suspend_timestamp=delete_timestamp,
            provider='provider1'
        )
        stack.status = state
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks[state],
            self.stacks[DELETE_IN_PROGRESS_STATE],
            self.stacks[DELETE_IN_PROGRESS_STATE],
            self.stacks[DELETE_IN_PROGRESS_STATE]
        ]

        # Run
        self.settings['task_timeouts']['retries'] = 3
        job = ReaperJob(self.settings)
        job.run()

        # Assert
        mock_provider.delete_stack.assert_called_with(stack_name, False)
        stack = Stack.objects.get(name=stack_name)
        self.assertEqual(stack.status, DELETE_FAILED_STATE)

    def test_dont_delete_if_age_is_zero(self):
        # Setup
        self.settings["delete_age"] = 0
        delete_delta = timezone.timedelta(days=15)
        delete_timestamp = timezone.now() - delete_delta
        state = 'RESUME_COMPLETE'
        stack_name = 'bogus_stack'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack_name,
            suspend_timestamp=delete_timestamp,
            provider='provider1',
            status=state
        )
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value

        # Run
        job = ReaperJob(self.settings)
        job.run()

        mock_provider.delete_stack.assert_not_called()
        stack = Stack.objects.get(name=stack_name)
        self.assertEqual(stack.status, state)

    def test_retry_deletion(self):
        # Setup
        delete_age = self.settings.get("delete_age")
        delete_delta = timezone.timedelta(days=(delete_age + 1))
        delete_timestamp = timezone.now() - delete_delta
        state = 'RESUME_COMPLETE'
        stack_name = 'bogus_stack'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack_name,
            suspend_timestamp=delete_timestamp,
            provider='provider1'
        )
        stack.status = state
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks[state],
            self.stacks[DELETE_FAILED_STATE],
            self.stacks[DELETE_FAILED_STATE],
            self.stacks[DELETE_FAILED_STATE]
        ]

        # Run
        job = ReaperJob(self.settings)
        job.run()

        mock_provider.delete_stack.assert_has_calls([
            call(stack_name, False),
            call(stack_name, False),
            call(stack_name, False)
        ])
        stack = Stack.objects.get(name=stack_name)
        self.assertEqual(stack.status, DELETE_FAILED_STATE)

    def test_destroy_zombies(self):
        # Setup
        delete_age = self.settings.get("delete_age")
        delete_delta = timezone.timedelta(days=(delete_age + 1))
        delete_timestamp = timezone.now() - delete_delta
        dont_delete_delta = timezone.timedelta(days=(delete_age - 1))
        dont_delete_timestamp = timezone.now() - dont_delete_delta
        stack_names = (
            'zombie_stack_1',
            'zombie_stack_2',
            'zombie_stack_3',
            'zombie_stack_4',
            'not_a_zombie_stack'
        )

        # Create zombie stacks
        for i in range(0, 4):
            _stack = Stack(
                student_id=self.student_id,
                course_id=self.course_id,
                name=stack_names[i],
                suspend_timestamp=delete_timestamp,
                status=DELETED_STATE
            )
            _stack.save()

        # Create living stack
        _stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            name=stack_names[4],
            suspend_timestamp=dont_delete_timestamp,
            status=CREATE_STATE
        )
        _stack.save()

        mock_provider = self.mocks["Provider"].init.return_value
        provider1_stacks = []
        for i in range(0, 3):
            provider1_stacks.append({
                "name": stack_names[i],
                "status": CREATE_STATE
            })
        provider2_stacks = []
        for i in range(3, 5):
            provider2_stacks.append({
                "name": stack_names[i],
                "status": CREATE_STATE
            })
        provider3_stacks = [{
            "name": "unknown",
            "status": CREATE_STATE
        }]
        mock_provider.get_stacks.side_effect = [
            provider1_stacks,
            provider2_stacks,
            provider3_stacks
        ]
        mock_provider.get_stack.side_effect = [
            {"name": stack_names[0], "status": CREATE_STATE},
            {"name": stack_names[0], "status": DELETED_STATE},
            {"name": stack_names[1], "status": CREATE_STATE},
            {"name": stack_names[2], "status": CREATE_STATE},
            {"name": stack_names[2], "status": DELETED_STATE},
            {"name": stack_names[3], "status": CREATE_STATE},
            {"name": stack_names[3], "status": DELETED_STATE},
        ]
        mock_provider.delete_stack.side_effect = [
            True,
            ProviderException(""),
            True,
            True
        ]
        self.settings["providers"] = {
            "provider1": {},
            "provider2": {},
            "provider3": {}
        }

        # Run
        job = ReaperJob(self.settings)
        job.run()

        # Assert
        mock_provider.delete_stack.assert_has_calls([
            call(stack_names[0], False),
            call(stack_names[1], False),
            call(stack_names[2], False),
            call(stack_names[3], False)
        ])
        self.assertNotIn(
            call(stack_names[4], False),
            mock_provider.delete_stack.mock_calls
        )
        self.assertNotIn(
            call("unknown", False),
            mock_provider.delete_stack.mock_calls
        )
        stack = Stack.objects.get(name=stack_names[1])
        self.assertEqual(stack.status, DELETE_FAILED_STATE)

    def test_exception_destroying_zombies(self):
        # Setup
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stacks.side_effect = ProviderException("")
        self.settings["providers"] = {"provider": {}}

        # Run
        job = ReaperJob(self.settings)
        job.run()

    def test_stack_log(self):
        # Setup
        suspend_timeout = self.settings.get("suspend_timeout")
        timedelta = timezone.timedelta(seconds=(suspend_timeout + 1))
        suspend_timestamp = timezone.now() - timedelta
        state = 'CREATE_COMPLETE'
        stack = Stack(
            student_id=self.student_id,
            course_id=self.course_id,
            suspend_timestamp=suspend_timestamp,
            provider='provider1',
            name=self.stack_name
        )
        stack.status = state
        stack.save()
        mock_provider = self.mocks["Provider"].init.return_value
        mock_provider.get_stack.side_effect = [
            self.stacks[state]
        ]

        # Run
        job = SuspenderJob(self.settings)
        job.run()

        # Assert
        stacklog = StackLog.objects.filter(stack_id=stack.id)
        states = [l.status for l in stacklog]
        expected_states = [state,
                           'SUSPEND_PENDING',
                           'SUSPEND_ISSUED']
        self.assertEqual(states, expected_states)
