/* tests/test_client/SpeechInput.test.js

import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import SpeechInput from '../src/components/SpeechInput';

describe('SpeechInput', () => {
  it('renders without crashing', () => {
    const { getByTestId } = render(<SpeechInput />);
    const speechInput = getByTestId('speech-input');
    expect(speechInput).toBeInTheDocument();
  });
});

*/