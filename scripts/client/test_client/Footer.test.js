/* tests/test_client/Footer.test.js

import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Footer from '../src/components/Footer';

describe('Footer', () => {
  it('renders without crashing', () => {
    const { getByTestId } = render(<Footer />);
    const footer = getByTestId('footer');
    expect(footer).toBeInTheDocument();
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

