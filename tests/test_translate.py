import io
import unittest
from unittest import mock
from core.translate import translate


class TestTranslate(unittest.TestCase):

    @mock.patch('core.translate.Translator')
    def test_translate_file(self, mock_translator):
        attrs = {'text.return_value': 'Quiero traducir esto'}
        mock_translator().translate.return_value = mock.Mock(text='Quiero traducir esto')
        output_file = io.StringIO()
        translated_text = translate(
            file=io.StringIO('I want to translate this'),
            output=output_file,
            source='en',
            dest='es'
        )
        mock_translator().translate.assert_called_once_with(
            'I want to translate this', dest='es', source='en'
        )
        self.assertEqual(translated_text, 'Quiero traducir esto')

if __name__ == '__main__':
    unittest.main()