/* tests/test_client/Cards.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import Cards from '../src/components/Cards';

test('renders Cards component', () => {
  render(<Cards />);
  const linkElement = screen.getByText(/learn more/i);
  expect(linkElement).toBeInTheDocument();
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