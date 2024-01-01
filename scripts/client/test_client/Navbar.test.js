/* tests/test_client/Navbar.test.js

import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Navbar from '../src/components/Navbar';

describe('Navbar', () => {
  it('renders without crashing', () => {
    const { getByTestId } = render(<Navbar />);
    const navbar = getByTestId('navbar');
    expect(navbar).toBeInTheDocument();
  });
});

*/