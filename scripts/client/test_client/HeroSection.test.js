/* tests/test_client/HeroSection.test.js

import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import HeroSection from '../src/components/HeroSection';

describe('HeroSection', () => {
  it('renders without crashing', () => {
    const { getByTestId } = render(<HeroSection />);
    const heroSection = getByTestId('hero-section');
    expect(heroSection).toBeInTheDocument();
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