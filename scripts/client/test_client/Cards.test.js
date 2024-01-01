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
