# Stage 1: Install dependencies and build the application
ARG NODE_VERSION=20.12.2
ARG PNPM_VERSION=9.0.1

FROM node:${NODE_VERSION}-alpine AS builder

# Install pnpm globally
RUN npm install -g pnpm@${PNPM_VERSION}

# Set working directory
WORKDIR /app

# Copy package.json and pnpm-lock.yaml (if available)
COPY package*.json ./
COPY pnpm-lock.yaml* ./

# Install dependencies
RUN pnpm install

# Copy the rest of the application code
COPY . .

# Build the Next.js app
RUN pnpm build

# Stage 2: Create a minimal image for running the app
FROM node:${NODE_VERSION}-alpine AS runner

# Install pnpm globally in the final stage
RUN npm install -g pnpm@${PNPM_VERSION}

# Set working directory
WORKDIR /app

# Copy necessary files from the builder stage
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules

# Expose port 3000
EXPOSE 3000

# Run the application
CMD ["pnpm", "start"]
