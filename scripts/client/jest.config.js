module.exports = {
    testEnvironment: 'jsdom',
    moduleNameMapper: {
      '^src/(.*)$': '<rootDir>/scripts/client/src/$1',
      '\\.css$': 'identity-obj-proxy',
    },
    transformIgnorePatterns: [
      '/node_modules/',
      '\\.css$',
    ],
  };
  