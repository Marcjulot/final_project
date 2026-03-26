import SwiftUI

struct QuoteView: View {
    let mood: Mood
    @State private var currentQuote: Quote

    init(mood: Mood) {
        self.mood = mood
        self._currentQuote = State(initialValue: mood.randomQuote())
    }

    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                Text(mood.emoji)
                    .font(.system(size: 64))
                    .padding(.top, 24)

                Text(mood.message)
                    .font(.body)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal)

                Text(mood.encouragement)
                    .font(.callout)
                    .fontWeight(.medium)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal)

                VStack(spacing: 12) {
                    Text("\"\(currentQuote.text)\"")
                        .font(.title3)
                        .italic()
                        .multilineTextAlignment(.center)

                    Text("— \(currentQuote.author)")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                }
                .padding(24)
                .frame(maxWidth: .infinity)
                .background(Color(.systemGray6))
                .cornerRadius(16)
                .padding(.horizontal)

                Button {
                    withAnimation(.easeInOut(duration: 0.3)) {
                        currentQuote = mood.randomQuote()
                    }
                } label: {
                    Label("New Quote", systemImage: "arrow.clockwise")
                        .font(.headline)
                        .padding(.horizontal, 24)
                        .padding(.vertical, 12)
                }
                .buttonStyle(.borderedProminent)
                .tint(.blue)

                Spacer()
            }
        }
        .navigationTitle(mood.displayName)
        .navigationBarTitleDisplayMode(.inline)
    }
}

#Preview {
    NavigationStack {
        QuoteView(mood: .happy)
    }
}
