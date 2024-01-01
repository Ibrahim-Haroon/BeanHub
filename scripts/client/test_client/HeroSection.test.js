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