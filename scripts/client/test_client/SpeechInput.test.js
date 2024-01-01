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

import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Order from '../src/components/Order';

describe('Order', () => {
  it('renders without crashing', () => {
    const { getByTestId } = render(<Order />);
    const order = getByTestId('order');
    expect(order).toBeInTheDocument();
  });
});